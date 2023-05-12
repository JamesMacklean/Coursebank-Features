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
    def get(self, request, format=None):
        """
        Returns the top 10 most enrolled courses.
        """
        most_enrolled_courses = CourseOverview.objects.all().order_by('-enrollment_count')[:10]
        serializer = MostPopularCoursesSerializer(most_enrolled_courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)