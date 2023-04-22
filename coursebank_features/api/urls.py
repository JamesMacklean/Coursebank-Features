from django.urls import path, include
from coursebank_features.api.views import *

urlpatterns = [

    ####################### COURSE TAGS #######################
    path('course_tag/', CourseTagViewSet, name='api_course_tag'),
    ####################### COURSE TAGS #######################
]