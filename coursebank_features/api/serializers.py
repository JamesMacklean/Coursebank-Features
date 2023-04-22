from rest_framework import serializers
from coursebank_features.models import *

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
    # course_id = serializers.SerializerMethodField()
    # course_display_name = serializers.SerializerMethodField() 
    primary_topic = PrimaryTopicSerializer()
    subtopic = SubTopicSerializer(many=True)
    skills = SkillSerializer(many=True)
    organization = OrganizationSerializer(many=True)

    class Meta:
        model = CourseTag
        fields = ['id', 'course_id', 'course_display_name', 'primary_topic', 'subtopic', 'skills', 'organization']
        
    # def get_course_id(self, obj):
    #     course_overview = obj.course_overview
    #     if course_overview is not None:
    #         return CourseOverviewSerializer(course_overview).data['id']
    #     else:
    #         return obj.id
        
    # def get_course_display_name(self, obj):
    #     course_overview = obj.course_overview
    #     if course_overview is not None:
    #         return course_overview.display_name
    #     else:
    #         return None
        