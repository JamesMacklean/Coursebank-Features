
from rest_framework import viewsets
from api.serializers import CourseTagSerializer
from coursebank_features.models import *

class CourseTagViewSet(viewsets.ModelViewSet):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer  