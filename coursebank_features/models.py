from django.db import models
from django.urls import reverse
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

####################### COURSE TAGS #######################
class CourseTag(models.Model):
    course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE)
    primary_topic = models.ForeignKey('PrimaryTopic', on_delete=models.CASCADE, null=True, blank=True)
    subtopic = models.ManyToManyField('Subtopic', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    organization = models.ManyToManyField('Organization', blank=True)

    class Meta:
        unique_together = ('course', 'primary_topic')


class PrimaryTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SubTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
##### COURSE BUNDLES #####

class SpecialCourse(models.Model):
    course_id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    long_description = models.TextField(blank=True, default="")
    image_url = models.CharField(max_length=255, default="")
    order = models.PositiveSmallIntegerField(default=0)
    course_bundle = models.ForeignKey(
        'CourseBundle',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="courses"
    )
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Special Courses"

    def __str__(self):
        return "{}: {}: {}".format(self.name, self.course_id, self.course_bundle.name)
    

class CourseBundle(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    long_description = models.TextField(blank=True, default="")
    card_description = models.TextField(blank=True, default="")
    image_url = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Bundles"
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name