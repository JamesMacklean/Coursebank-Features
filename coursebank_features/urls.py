"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path, include
from rest_framework import routers
from coursebank_features.views.views import *
from coursebank_features.api.views import *

router = routers.DefaultRouter()
router.register(r'course_tag', CourseTagViewSet)

urlpatterns = [
    path('features/', main, name='main'),
    ####################### API #######################
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ####################### COURSE TAGS #######################
    path('course_tag/', course_tag, name='course_tag'),
    path('course_tag/add/', add_course_tag, name='add_course_tag'),
    path('course_tag/add/primary_topic/', add_primary_topic, name='add_primary_topic'),
    path('course_tag/add/subtopic/', add_subtopic, name='add_subtopic'),
    path('course_tag/add/skill/', add_skill, name='add_skill'),
    path('course_tag/add/organization/', add_organization, name='add_organization'),
]