from django.urls import path, include
from rest_framework import routers
from coursebank_features.api.views import *

router = routers.DefaultRouter()
router.register(r'course-tag', CourseTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
