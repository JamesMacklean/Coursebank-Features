from django.db import models
from taggit.managers import TaggableManager
from course_overviews.models import CourseOverview

class CourseOverviewTags(CourseOverview):
    
    tags = TaggableManager()
