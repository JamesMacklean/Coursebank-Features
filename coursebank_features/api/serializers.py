from rest_framework import serializers
from coursebank_features.models import *

from common.djangoapps.student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

####################### COURSE TAGS #######################
class PrimaryTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryTopic
        fields = ['name']

class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTopic
        fields = ['name']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name']

class CourseTagSerializer(serializers.ModelSerializer):
    course_id = serializers.UUIDField(source='course.id')
    course_display_name = serializers.CharField(source='course.display_name')
    primary_topic = PrimaryTopicSerializer()
    subtopic = SubTopicSerializer(many=True)
    skills = SkillSerializer(many=True)
    organization = OrganizationSerializer(many=True)

    class Meta:
        model = CourseTag
        fields = ['id', 'course_id', 'course_display_name', 'primary_topic', 'subtopic', 'skills', 'organization']
        
class MostPopularCoursesSerializer(serializers.Serializer):
    course_id = serializers.CharField()
    course_name = serializers.CharField()
    enrollment_count = serializers.IntegerField()

    class Meta:
        model = CourseOverview
        fields = ('id', 'course_name', 'enrollment_count')

class TrendingCoursesSerializer(serializers.Serializer):
    course_id = serializers.CharField()
    course_name = serializers.CharField()
    enrollment_count = serializers.IntegerField()

    class Meta:
        model = CourseOverview
        fields = ('id', 'course_name', 'enrollment_count')
  
class FreeCoursesSerializer(serializers.Serializer):
    course_id = serializers.CharField()
    course_name = serializers.CharField()
    enrollment_count = serializers.IntegerField()

    class Meta:
        model = CourseOverview
        fields = ('id', 'course_name', 'enrollment_count')
        
class LatestCoursesSerializer(serializers.Serializer):
    course_id = serializers.CharField()
    course_name = serializers.CharField()
    date_published = serializers.SerializerMethodField()

    def get_date_created(self, instance):
        return instance['date_published'].strftime('%Y-%m-%d %H:%M:%S')

class CourseBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseBundle
        fields = ('name','slug', 'long_description', 'image_url')        
        
