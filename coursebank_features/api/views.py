from django.utils import timezone
from datetime import timedelta, datetime
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from coursebank_features.api.serializers import *
from coursebank_features.api.variables import *
from coursebank_features.models import *

from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
class CourseTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        course_tags = CourseTag.objects.all()
        serializer = CourseTagSerializer(course_tags, many=True)
        return Response(serializer.data)
    
class MostPopularCoursesAPIView(APIView):
    def get(self, request):
        try:
            # Get all course overviews
            course_overviews = CourseOverview.objects.all()
            # course_overviews = CourseOverview.objects.exclude(id__in=EXCLUDED_COURSES)
            
            # Get enrollment counts for each course
            enrollments = []
            for course_overview in course_overviews:
                course_id = course_overview.id
                if course_id in EXCLUDED_COURSES:
                    continue
            
                enrollment_end = course_overview.enrollment_end
                if enrollment_end is None or enrollment_end > timezone.now():
                    enrollment_count = CourseEnrollment.objects.filter(
                        course_id=course_overview.id,
                        is_active=True
                    ).count()
                    enrollments.append({
                        'course_id': course_overview.id,
                        'course_name': course_overview.display_name,
                        'enrollment_count': enrollment_count,
                    })

            # Sort the enrollments list by enrollment count in descending order
            sorted_enrollments = sorted(enrollments, key=lambda x: x['enrollment_count'], reverse=True)

            # Return the top 10 courses with the highest enrollment count
            top_enrollments = sorted_enrollments[:10]

            # Serialize the enrollment data
            serializer = MostPopularCoursesSerializer(top_enrollments, many=True)

            # Return the enrollment data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)

        except CourseOverview.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class TrendingCoursesAPIView(APIView):
    def get(self, request):
        try:
            course_enrollments = CourseEnrollment.objects.filter(created__gte=timezone.now() - timezone.timedelta(days=30))
            
            # Count enrollments for each course in the last 30 days
            enrollments = {}
            for course_enrollment in course_enrollments:
                course_id = course_enrollment.course.id
                enrollments[course_id] = enrollments.get(course_id, 0) + 1

            # Get course overviews for the enrolled courses
            course_overviews = CourseOverview.objects.filter(id__in=enrollments.keys())

            # Create a list of course data with enrollment count
            trending_courses = []
            for course_overview in course_overviews:
                course_id = course_overview.id
                if course_id in EXCLUDED_COURSES:
                    continue
                enrollment_count = enrollments[course_id]
                trending_courses.append({
                    'course_id': course_id,
                    'course_name': course_overview.display_name,
                    'enrollment_count': enrollment_count,
                })

            # Sort the trending courses list by enrollment count in descending order
            sorted_courses = sorted(trending_courses, key=lambda x: x['enrollment_count'], reverse=True)

            # Return the trending courses data as a JSON response
            return Response(sorted_courses, status=status.HTTP_200_OK)

        except CourseOverview.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class FreeCoursesAPIView(APIView):
    def get(self, request):
        try:
            # Get all course overviews
            course_overviews = CourseOverview.objects.all()

            # Get enrollments for each course in the last 30 days
            enrollments = []
            for course_overview in course_overviews:
                course_id = course_overview.id
                if course_id in EXCLUDED_COURSES:
                    continue
                
                enrollment_end = course_overview.enrollment_end
                if enrollment_end is None or enrollment_end > timezone.now():
                    enrollment_count = CourseEnrollment.objects.filter(
                        course_id=course_overview.id,
                        is_active=True,
                        mode="honor",
                    ).count()
                    enrollments.append({
                        'course_id': course_overview.id,
                        'course_name': course_overview.display_name,
                        'enrollment_count': enrollment_count,
                    })

            # Sort the enrollments list by enrollment count in descending order
            sorted_enrollments = sorted(enrollments, key=lambda x: x['enrollment_count'], reverse=True)

            if sorted_enrollments:
                # Get the most enrolled course in the last 30 days
                most_enrolled_course = sorted_enrollments[:10]

                # Serialize the enrollment data
                serializer = FreeCoursesSerializer(most_enrolled_course, many=True)

            # Return the enrollment data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)

        except CourseOverview.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

        except CourseOverview.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

class LatestCoursesAPIView(APIView):
    def get(self, request):
        try:
            
            # Get top 10 newest courses
            course_overviews = CourseOverview.objects.order_by('-created')[:10]
            
            courses = []
            for course_overview in course_overviews:
                course_id = course_overview.id
                if course_id in EXCLUDED_COURSES:
                    continue
                
                courses.append({
                    'course_id': course_overview.id,
                    'course_name': course_overview.display_name,
                    'date_created': course_overview.created.strftime('%Y-%m-%d %H:%M:%S'),
                })
                
            # Serialize course data
            serializer = LatestCoursesSerializer(course_overviews, many=True)

            # Return course data
            return Response(serializer.data, status=status.HTTP_200_OK)

        except CourseOverview.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

class CourseBundleListAPIView(APIView):
    def get(self, request):
        bundles = CourseBundle.objects.all()
        serializer = CourseBundleSerializer(bundles, many=True)
        return Response(serializer.data)