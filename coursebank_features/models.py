from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

####################### COURSE TAGS #######################
class CourseTag(models.Model):
    course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE)
    primary_topic = models.ForeignKey('PrimaryTopic', on_delete=models.CASCADE, null=True, blank=True)
    subtopic = models.ManyToManyField('Subtopic', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    organization = models.ManyToManyField('Organization', blank=True)

class PrimaryTopic(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class SubTopic(models.Model):
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

####################### COURSE TAGS #######################