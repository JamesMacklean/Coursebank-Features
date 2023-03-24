"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path
from django.conf.urls import url
from .views import views

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="coursebank_features/base.html")),
    # path('features/', views.features_dashboard, name='features_dashboard'),
    url(r'^features/$', views.features_dashboard, name='features_dashboard'),
]