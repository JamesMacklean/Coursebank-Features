from django.contrib import admin
from .models import (CourseTopic, CourseSkill, CourseSubTopic, CourseOrganization)

@admin.register(CourseTopic)
class CourseTopicAdmin (admin.ModelAdmin):
    list_display = ['course', 'primary_topic']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('topic')
    
    def primary_topic(self, obj):
        return ", ".join(o for o in obj.topic.names())
    
@admin.register(CourseSkill)
class CourseSkillAdmin (admin.ModelAdmin):
    list_display = ['course', 'skills']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('skills')
    
    def skills(self, obj):
        return ", ".join(o for o in obj.skills.names())
    
@admin.register(CourseSubTopic)
class CourseSubTopicAdmin (admin.ModelAdmin):
    list_display = ['course', 'subtopics']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('subtopics')
    
    def subtopics(self, obj):
        return ", ".join(o for o in obj.subtopics.names())
@admin.register(CourseOrganization)
class CourseOrganizationAdmin (admin.ModelAdmin):
    list_display = ['course', 'organization']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('organization')
    
    def organization(self, obj):
        return ", ".join(o for o in obj.organization.names())




