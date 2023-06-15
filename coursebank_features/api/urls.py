from django.urls import path, include
from rest_framework import routers
from coursebank_features.api.views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('course-tag/', CourseTagAPIView.as_view(), name='course-tag'),
    path('course-bundles/', CourseBundleListAPIView.as_view(), name='course_bundle_list'),
    path('courses/most-popular/', MostPopularCoursesAPIView.as_view(), name='most-popular-courses'),
    path('courses/trending/', TrendingCoursesAPIView.as_view(), name='trending-courses'),
    path('courses/free/', FreeCoursesAPIView.as_view(), name='free-courses'),
    path('courses/latest/', LatestCoursesAPIView.as_view(), name='latest-courses'),
    path('courses/', CoursesAPIView.as_view(), name='courses'),

]
