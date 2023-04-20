"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path
from .views import views

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    path('features-dashboard/', views.dashboard, name='dashboard'),
    
    ####################### COURSE TAGS #######################
    path('create/subtopic', views.SubtopicCreateView.as_view(), name='create_subtopic'),
    path('create/primarytopic', views.PrimaryTopicCreateView.as_view(), name='create_primarytopic'),
    path('create/skill', views.SkillCreateView.as_view(), name='create_skill'),
    path('create/organization', views.OrganizationCreateView.as_view(), name='create_organization'),
    ####################### COURSE TAGS #######################
]