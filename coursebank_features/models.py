from django.db import models
from taggit.managers import TaggableManager
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class CourseTags(models.Model):
    
    course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE)
    tags = TaggableManager()

