from django.db import models
from taggit.managers import TaggableManager
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

# class CourseTopic(models.Model):
    
#     course = models.ForeignKey(
#         CourseOverview, on_delete=models.CASCADE
#         )
#     topic = TaggableManager()

#     def __str__(self):
#         return "{}: {}".format(self.course, self.topic)

class CourseOverviewExtended(models.Model):
    course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE)
    primary_topic = models.CharField(max_length=255, null=True, blank=True)
    subtopic = models.ManyToManyField('Subtopic', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    organization = models.ManyToManyField('Organization', blank=True)


class PrimaryTopic(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
class Subtopic(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
class Skill(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name