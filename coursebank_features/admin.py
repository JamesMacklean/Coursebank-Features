from django.contrib import admin
from .models import *

class CourseTagAdmin(admin.ModelAdmin):
    list_display = ['course', 'primary_topic', 'get_subtopics', 'get_skills', 'get_organization']

    def get_subtopics(self, obj):
        return ", ".join([str(subtopic) for subtopic in obj.subtopic.all()])
    
    def get_skills(self, obj):
        return ", ".join([str(skill) for skill in obj.skills.all()])
    
    def get_organization(self, obj):
        return ", ".join([str(organization) for organization in obj.organization.all()]) 

####################### COURSE TAGS #######################
@admin.register(CourseTag)
class CourseTagAdmin (CourseTagAdmin):
    pass

@admin.register(PrimaryTopic)
class PrimaryTopicAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    list_display = ('__str__',)    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(SpecialCourse)
class SpecialCourseAdmin(admin.ModelAdmin):
    pass
@admin.register(CourseBundle)
class CourseBundleAdmin(admin.ModelAdmin):
    pass