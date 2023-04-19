from django.db import models
from taggit.managers import TaggableManager
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class CourseOverviewTags(CourseOverview):
    
    tags = TaggableManager()
