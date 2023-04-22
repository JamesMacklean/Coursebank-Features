from rest_framework import viewsets

from coursebank_features.api.serializers import *
from coursebank_features.models import *

####################### COURSE TAGS #######################
class CourseTagViewSet(viewsets.ModelViewSet):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer 
####################### COURSE TAGS ####################### 