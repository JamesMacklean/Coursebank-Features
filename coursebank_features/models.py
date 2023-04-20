from django.db import models
from taggit.managers import TaggableManager
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class CourseTag(models.Model):
    
    course = models.ForeignKey(
        CourseOverview, on_delete=models.CASCADE,
        null=True, blank=True,
        )
    tags = TaggableManager()

    def __str__(self):
        return self.name
    
