from rest_framework import serializers
from coursebank_features.models import *

from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

####################### API ###########################
class CoursesSerializer(serializers.Serializer):
    course_id = serializers.CharField()
    course_name = serializers.CharField()
    enrollment_count = serializers.IntegerField()
    mode = serializers.CharField()
    date_published = serializers.SerializerMethodField()

    class Meta:
        model = CourseOverview
        fields = ('id', 'course_name', 'enrollment_count', 'published_at', 'mode')

    def get_date_published(self, instance):
        return instance['date_published'].strftime('%Y-%m-%d %H:%M:%S')
    
# class CourseBundleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseBundle
#         fields = ('name','slug', 'long_description', 'image_url')        
        
