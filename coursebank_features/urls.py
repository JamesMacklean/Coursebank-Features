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
    ####################### API ###########################
    path('api/', include('coursebank_features.api.urls')),
    ####################### COURSE BUNDLES ################
    # re_path(r'^bundles/(?P<slug>[\w-]+)/$', bundles, name='bundles'),
    ####################### PARTNERS ######################
    re_path(r'^partners/$', PartnersCatalogView, name='partners-catalog'),
    re_path(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/$', PartnerView, name='partner'),
    re_path(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/course/{}/$'.format(settings.COURSE_ID_PATTERN), PartnerCourseView, name='partner-course'),
    re_path(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/expert/(?P<expert_id>\d+)$', ExpertView, name='expert'),
    path('lakip/', TemplateView.as_view(template_name="partner/new-lakip-landing.html"), name='lakip'),
]