from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from coursebank_features.api.serializers import *
from coursebank_features.models import *

from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class CourseTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        course_tags = CourseTag.objects.all()
        serializer = CourseTagSerializer(course_tags, many=True)
        return Response(serializer.data)
    
class MostPopularCoursesList(generics.ListAPIView):
    """
    API endpoint that returns the top 10 most popular courses based on enrollment count.
    """
    serializer_class = CourseOverviewSerializer

    def get_queryset(self):
        return CourseOverview.objects.order_by('-enrollment_count')[:10]
