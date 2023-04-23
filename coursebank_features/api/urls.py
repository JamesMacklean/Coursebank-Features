from django.urls import path, include
from rest_framework import routers
from coursebank_features.api.views import *

router = routers.DefaultRouter()
router.register(r'course-tag', CourseTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('most-popular/', MostPopularCoursesAPI.as_view(), name='most-popular-courses-api'),
    path('free-courses/', FreeCoursesAPI.as_view(), name='free-courses-api'),
    path('trending-courses/', TrendingCoursesAPI.as_view(), name='trending-courses-api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
