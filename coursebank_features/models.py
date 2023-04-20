from django.db import models
from taggit.managers import TaggableManager
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class CourseTopic(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    topics = TaggableManager()

    def __str__(self):
        return self.name
    
class CourseSkill(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    skills = TaggableManager()

    def __str__(self):
        return self.name

class CourseSubTopic(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    subtopic = TaggableManager()

    def __str__(self):
        return self.name

class CourseOrganization(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    organization = TaggableManager()
    
    def __str__(self):
        return self.name
