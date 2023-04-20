from django.db import models
from taggit.managers import TaggableManager
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class CourseTopic(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    topic = TaggableManager()

    def __str__(self):
        return "{}: {}".format(self.course, self.topic)
    
class CourseSkill(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    skills = TaggableManager()

    def __str__(self):
        return "{}: {}".format(self.course, self.skills)

class CourseSubTopic(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    subtopics = TaggableManager()

    def __str__(self):
        return "{}: {}".format(self.course, self.subtopics)

class CourseOrganization(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE
        )
    organization = TaggableManager()
    
    def __str__(self):
        return "{}: {}".format(self.course, self.organization)
