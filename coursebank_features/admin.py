from django.contrib import admin
from .models import *

@admin.register(CourseOverviewExtended)
class CourseOverviewExtendedAdmin (admin.ModelAdmin):
    list_display = ['course', 'primary_topic', 'get_subtopics', 'get_skills', 'organization']

    # def get_queryset(self, request):
    #     return super().get_queryset(request).prefetch_related('topic')
    
    def get_subtopics(self, obj):
        return ", ".join([str(subtopic) for subtopic in obj.subtopic.all()])
    
    def get_skills(self, obj):
        return ", ".join([str(skill) for skill in obj.skills.all()])
    
@admin.register(PrimaryTopic)
class PrimaryTopicAdmin (admin.ModelAdmin):
    list_display = ('__str__',)
    
@admin.register(Subtopic)
class SubTopicAdmin (admin.ModelAdmin):
    list_display = ('__str__',)

    
@admin.register(Skill)
class SkillAdmin (admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(Organization)
class OrganizationAdmin (admin.ModelAdmin):
    list_display = ('__str__',)




