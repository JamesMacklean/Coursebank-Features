from django.urls import path, include
from rest_framework import routers
from coursebank_features.api.views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('course-bundles/', CourseBundleListAPIView.as_view(), name='course_bundle_list'),
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('users/', UserListView.as_view(), name='user-list'),


]
