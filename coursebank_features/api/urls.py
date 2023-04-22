from django.urls import path, include
from coursebank_features.api.views import *

urlpatterns = [

    ####################### COURSE TAGS #######################
    path('course_tag/', CourseTagViewSet.as_view(), name='api_course_tag'),
    ####################### COURSE TAGS #######################
]