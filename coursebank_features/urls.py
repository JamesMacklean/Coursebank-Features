"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path
from .views.views import *

urlpatterns = [
    path('features/', main, name='main'),
    
    ####################### COURSE TAGS #######################
    path('course_tag/add/', add_course_tag, name='add_course_tag'),
    path('course_tag/create/', CourseTagCreateView.as_view(), name='course_tag_create'),
    ####################### COURSE TAGS #######################
]