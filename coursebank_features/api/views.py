from rest_framework.views import APIView
from rest_framework.response import Response

from coursebank_features.api.serializers import *
from coursebank_features.models import *

####################### COURSE TAGS #######################
# class CourseTagViewSet(viewsets.ModelViewSet):
#     queryset = CourseTag.objects.all()
#     serializer_class = CourseTagSerializer 
    
class CourseTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        course_tags = CourseTag.objects.all()
        serializer = CourseTagSerializer(course_tags, many=True)
        return Response(serializer.data)