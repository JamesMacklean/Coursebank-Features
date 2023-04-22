from rest_framework import serializers
from coursebank_features.models import *

####################### COURSE TAGS #######################
class PrimaryTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryTopic
        fields = '__all__'

class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTopic
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class CourseTagSerializer(serializers.ModelSerializer):
    course_id = serializers.UUIDField(source='course.course_id')
    course_display_name = serializers.CharField(source='course.display_name')
    primary_topic = PrimaryTopicSerializer()
    subtopic = SubTopicSerializer(many=True)
    skills = SkillSerializer(many=True)
    organization = OrganizationSerializer(many=True)

    class Meta:
        model = CourseTag
        fields = ['id','course_id', 'course_display_name', 'primary_topic', 'subtopic', 'skills', 'organization']
