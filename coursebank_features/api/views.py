from rest_framework import viewsets, generics
from django.db.models import Count
from datetime import datetime, timedelta

from coursebank_features.api.serializers import *
from coursebank_features.models import *
from common.djangoapps.course_modes.models import CourseMode
from common.djangoapps.student.models import CourseEnrollment

####################### COURSE TAGS #######################
class CourseTagViewSet(viewsets.ModelViewSet):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer 
    
class MostPopularCoursesAPI(generics.ListAPIView):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        return CourseEnrollment.objects.values('course', 'course__name') \
                .annotate(enrollment_count=Count('id')) \
                .order_by('-enrollment_count')
                
class FreeCoursesAPI(generics.ListAPIView):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        audit_mode = CourseMode.AUDIT
        return CourseMode.objects.filter(mode=audit_mode).values('course', 'course__name')

class TrendingCoursesAPI(generics.ListAPIView):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        current_month = datetime.now().month
        current_year = datetime.now().year
        return CourseEnrollment.objects.filter(created__year=current_year, created__month=current_month) \
                .values('course', 'course__name') \
                .annotate(enrollment_count=Count('id')) \
                .order_by('-enrollment_count')