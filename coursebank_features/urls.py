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
    ####################### COURSE TAGS #######################
]