from django.urls import path, include
from rest_framework import routers
from coursebank_features.api.views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('course-tag/', CourseTagAPIView.as_view(), name='course-tag'),
    path('courses/most-popular/', MostPopularCoursesAPIView.as_view(), name='most-popular-courses'),
    path('courses/trending/', MostPopularCoursesAPIView.as_view(), name='trending-courses'),

]
