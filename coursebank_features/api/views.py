from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# publicized API
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
# --------------
from coursebank_features.api.serializers import *
from coursebank_features.api.variables import *

from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.content.learning_sequences.models import LearningContext


class CourseTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        course_tags = CourseTag.objects.all()
        serializer = CourseTagSerializer(course_tags, many=True)
        return Response(serializer.data)

# publicized API
@permission_classes([AllowAny])
class MostPopularCoursesAPIView(APIView):
    def get(self, request):
        try:
            # Get all course overviews
            course_overviews = CourseOverview.objects.exclude(id__in=EXCLUDED_COURSES)
            
            # Get enrollment counts for each course
            enrollments = []
            for course_overview in course_overviews:                    
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
        
# publicized API
@permission_classes([AllowAny])
class TrendingCoursesAPIView(APIView):
    def get(self, request):
        # try:
            # Get the course enrollments in the last 120 days
            course_enrollments = CourseEnrollment.objects.filter(created__gte=timezone.now() - timezone.timedelta(days=30))
            
            if course_enrollments:
                enrollments = {}
                for course_enrollment in course_enrollments:
                    course_key = course_enrollment.course                
                    if str(course_key) in EXCLUDED_COURSES:
                        continue
                    enrollments[str(course_key)] = enrollments.get(str(course_key), 0) + 1
                
                # Iterate over the course_overviews
                trending_courses = []
                course_overviews = CourseOverview.objects.filter(id__in=enrollments.keys())
                
                for course_overview in course_overviews:
                    enrollment_count = enrollments.get(str(course_overview.id),0)

                    if enrollment_count:
                        trending_courses.append({
                            'course_id': course_overview.id,
                            'course_name': course_overview.display_name,
                            'enrollment_count': enrollment_count,
                        })

                # Sort the trending courses by enrollment count in descending order
                sorted_courses = sorted(trending_courses, key=lambda x: x['enrollment_count'], reverse=True)

                # Get the top 10 trending courses
                top_trending_courses = sorted_courses[:10]

                # Serialize the enrollment data
                serializer = TrendingCoursesSerializer(top_trending_courses, many=True)

                # Return the enrollment data as a JSON response
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                try:
                    # Get all course overviews
                    course_overviews = CourseOverview.objects.exclude(id__in=EXCLUDED_COURSES)
                    
                    # Get enrollment counts for each course
                    enrollments = []
                    for course_overview in course_overviews:                    
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
                    serializer = TrendingCoursesSerializer(top_enrollments, many=True)

                    # Return the enrollment data as a JSON response
                    return Response(serializer.data, status=status.HTTP_200_OK)

                except CourseOverview.DoesNotExist:
                    return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
                
        # except CourseOverview.DoesNotExist:
        #    return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

# publicized API
@permission_classes([AllowAny])
class FreeCoursesAPIView(APIView):
    def get(self, request):
        try:
            # Get all course overviews
            course_overviews = CourseOverview.objects.exclude(id__in=EXCLUDED_COURSES)

            # Get enrollments for each course in the last 30 days
            enrollments = []
            for course_overview in course_overviews:
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

# publicized API
@permission_classes([AllowAny])
class LatestCoursesAPIView(APIView):
    def get(self, request):
        try:
            
            # Get top 10 newest courses
            course_overviews = LearningContext.objects.exclude(context_key__in=EXCLUDED_COURSES).order_by('published_at')[:10]
    
            courses = []
            for course_overview in course_overviews:
                
                courses.append({
                    'course_id': course_overview.context_key,
                    'course_name': course_overview.title,
                    'date_published': course_overview.published_at,
                })
                
            # Serialize course data
            serializer = LatestCoursesSerializer(courses, many=True)

            # Return course data
            return Response(serializer.data, status=status.HTTP_200_OK)

        except LearningContext.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class CourseBundleListAPIView(APIView):
    def get(self, request):
        bundles = CourseBundle.objects.all()
        serializer = CourseBundleSerializer(bundles, many=True)
        return Response(serializer.data)
