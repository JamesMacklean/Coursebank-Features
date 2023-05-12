from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from coursebank_features.api.serializers import *
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

            # Get enrollment counts for each course
            enrollments = []
            for course_overview in course_overviews:
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