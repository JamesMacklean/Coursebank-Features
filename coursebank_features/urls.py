"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path
from .views import views

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    path('dashboard/', views.dashboard, name='dashboard'),
]