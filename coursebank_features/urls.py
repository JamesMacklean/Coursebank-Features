"""
URLs for coursebank_features.
"""
# from django.urls import re_path  # pylint: disable=unused-import
# from django.views.generic import TemplateView  # pylint: disable=unused-import

from django.urls import path, include, re_path
from coursebank_features.views.views import *
from .api.views import *
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('features/', main, name='main'),
    ########################### API ###########################
    path('api/', include('coursebank_features.api.urls')),
    ####################### COURSE TAGS #######################
    path('course-tag/', course_tag, name='course-tag'),
    path('course-tag/add/', add_course_tag, name='add-course-tag'),
    path('course-tag/add/primary-topic/', add_primary_topic, name='add-primary-topic'),
    path('course-tag/add/subtopic/', add_subtopic, name='add-subtopic'),
    path('course-tag/add/skill/', add_skill, name='add-skill'),
    path('course-tag/add/organization/', add_organization, name='add-organization'),
    ####################### COURSE BUNDLES #######################
    re_path(r'^bundles/(?P<slug>[\w-]+)/$', bundles, name='bundles'),
    ####################### PARTNER #######################
    re_path(r'^partners/$', PartnersCatalogView, name='partners-catalog'),
    re_path(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/$', PartnerView, name='partner'),
    re_path(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/course/{}/$'.format(settings.COURSE_ID_PATTERN), PartnerCourseView, name='partner-course'),
    re_path(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/expert/(?P<expert_id>\d+)$', ExpertView, name='expert'),
    path('lakip/', TemplateView.as_view(template_name="partner/lakip-landing.html"), name='lakip'),
    path('categories/', TemplateView.as_view(template_name="categories.html"), name='categories'),
]