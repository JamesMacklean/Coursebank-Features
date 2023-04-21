"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path
from .views import views

urlpatterns = [
    path('features/', views.main, name='main'),
    
    ####################### COURSE TAGS #######################
    path('course_tag/', views.course_tag, name='course_tag'),
    path('course_tag/add/', views.add_course_tag, name='add_course_tag'),
    path('course_tag/add/primary_topic/', views.add_primary_topic, name='add_primary_topic'),
    path('course_tag/add/subtopic/', views.add_subtopic, name='add_subtopic'),
    path('course_tag/add/skill/', views.add_skill, name='add_skill'),
    path('course_tag/add/organization/', views.add_organization, name='add_organization'),
    ####################### COURSE TAGS #######################
]