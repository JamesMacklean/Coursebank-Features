from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from coursebank_features.api.serializers import *
from coursebank_features.models import *

from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
class CourseTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        course_tags = CourseTag.objects.all()
        serializer = CourseTagSerializer(course_tags, many=True)
        return Response(serializer.data)
    
class MostPopularCoursesAPIView(generics.ListAPIView):
    """
    API endpoint that returns top 10 most enrolled courses
    """
    permission_classes = (AllowAny,)
    serializer_class = MostPopularCoursesSerializer

    def get_queryset(self):
        return CourseEnrollment.objects.filter(is_active=True).values('course_id').annotate(
            enrollment_count=models.Count('id')
        ).order_by('-enrollment_count')[:10].values_list('course_id', flat=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)