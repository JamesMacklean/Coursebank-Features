"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path, include
from .views.views import *
from .api.views import *

urlpatterns = [
    path('features/', main, name='main'),
    path('api/', include('coursebank_features.api.urls')),
    ####################### COURSE TAGS #######################
    path('course-tag/', course_tag, name='course-tag'),
    path('course-tag/add/', add_course_tag, name='add-course-tag'),
    path('course-tag/add/primary_topic/', add_primary_topic, name='add-primary-topic'),
    path('course-tag/add/subtopic/', add_subtopic, name='add-subtopic'),
    path('course-tag/add/skill/', add_skill, name='add-skill'),
    path('course-tag/add/organization/', add_organization, name='add-organization'),
]