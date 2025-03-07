from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
    
####################### COURSE BUNDLES ################

# class SpecialCourse(models.Model):
#     course_id = models.CharField(max_length=255, null=True, blank=True)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     short_description = models.CharField(max_length=255, null=True, blank=True)
#     long_description = models.TextField(blank=True, default="")
#     image_url = models.CharField(max_length=255, default="")
#     order = models.PositiveSmallIntegerField(default=0)
#     course_bundle = models.ForeignKey(
#         'CourseBundle',
#         on_delete=models.CASCADE,
#         null=True, blank=True,
#         related_name="courses"
#     )
#     is_active = models.BooleanField(default=True)
#     class Meta:
#         ordering = ['order']
#         verbose_name_plural = "Special Courses"

#     def __str__(self):
#         return "{}: {}: {}".format(self.name, self.course_id, self.course_bundle.name)
    
# class CourseBundle(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)
#     short_description = models.CharField(max_length=255, null=True, blank=True)
#     long_description = models.TextField(blank=True, default="")
#     card_description = models.TextField(blank=True, default="")
#     image_url = models.CharField(max_length=255)
#     order = models.PositiveSmallIntegerField(default=0)
#     is_active = models.BooleanField(default=True)
#     class Meta:
#         ordering = ['order']
#         verbose_name_plural = "Bundles"
        
#     def __str__(self):
#         return self.name
    
####################### PARTNERS ################

class Partner(models.Model):
    org = models.CharField(
        max_length=255,
        help_text='organization short name ex. OrgX used when creating courses',
        unique=True)
    name = models.CharField(max_length=255,default='No name')
    slugName = models.SlugField(max_length=255,editable=False, default=slugify(name),unique=True)
    description = models.TextField(default='No description set.')
    logo = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for logo images. This logo will be used on partner pages.',
        null=True, blank=True, max_length=255)
    logo_url = models.URLField(max_length=500, blank=True, default="")
    banner = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for banner images. This banner will be used on partner pages.',
        null=True, blank=True, max_length=255)
    banner_url = models.URLField(max_length=500, blank=True, default="")
    banner_mobile_url = models.URLField(max_length=500, blank=True, default="")
    banner_tablet_url = models.URLField(max_length=500, blank=True, default="")
    info = models.TextField(default="")
    website_url = models.TextField(default="")
    socmed_url = models.TextField(default="")
    is_active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=0)
    cert_desc = models.TextField(blank=True, default="")

    class Meta:
        ordering = ['-ranking']

    def save(self, *args, **kwargs):
        self.slugName = slugify(self.name)
        super(Partner, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PartnerCourse(models.Model):
    course_id = models.CharField(max_length=255,primary_key=True)
    partner = models.ForeignKey(
        'Partner',
        related_name='partner_course',
        help_text='partner/organization associated with this course',
        on_delete=models.CASCADE
        )
    experts = models.ManyToManyField(
        'Expert',
        related_name='partner_course',
        help_text='Experts that facilitate this course',
        blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def is_starting(self):
        get_course = CourseOverview.objects.filter(id=self.course_id)
        if get_course is not None:
            return date.today() < get_course.start
        else:
            return None

    def __str__(self):
        return self.course_id

    # def save(self, *args, **kwargs):
    #     self.slugTitle = slugify(self.title)
    #     super(Course, self).save(*args, **kwargs)

class Expert(models.Model):
    name = models.CharField(max_length=75,default='No name')
    description = models.TextField(default='No description set.')
    position = models.CharField(max_length=255, default='Expert')
    position_org = models.CharField(max_length=255, default='')
    profilePic = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for profile images. This image will be used on partner pages.',
        null=True, blank=True, max_length=255)
    profile_pic_url = models.URLField(max_length=500, blank=True, default="")
    partner = models.ForeignKey(
        'Partner',
        related_name='expert',
        help_text='partner/organization associated with this expert',
        on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name