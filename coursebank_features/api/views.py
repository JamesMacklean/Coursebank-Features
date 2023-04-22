from rest_framework import viewsets
from django.contrib.admin.views.decorators import staff_member_required

from coursebank_features.api.serializers import *
from coursebank_features.models import *


####################### COURSE TAGS #######################
@staff_member_required
class CourseTagViewSet(viewsets.ModelViewSet):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer 
####################### COURSE TAGS ####################### 