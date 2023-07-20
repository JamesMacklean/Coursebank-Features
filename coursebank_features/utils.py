import csv
from datetime import datetime
from time import strftime
from django.utils import timezone
import logging
import unicodecsv

from django.db import connection
from django.core.mail import send_mail, EmailMessage

from django.http import Http404
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from opaque_keys.edx.keys import CourseKey
from common.djangoapps.student.models import CourseEnrollment, UserProfile
from lms.djangoapps.certificates.api import get_certificate_for_user, GeneratedCertificate
from openedx.core.djangoapps.course_groups.models import CourseUserGroup

LOGGER = logging.getLogger(__name__)

def export_learner_profiles(email_address=None):
    tnow = datetime.now().strftime('%Y-%m-%d')
    profiles = User.objects.all()

    fields = ['id', 'username', 'name', 'email', 'date_joined', 'is_active']

    output_file = '/home/ubuntu/tempfiles/generated_certificates{}.csv'.format(tnow)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for p in profiles:
            user = User.objects.get(id=User.user_id)
            data = {
                'id': p.user.id,
                'username': p.username,
                'name': p.name,
                'email': p.email,
                'date_joined': user.date_joined,
                'is_active': p.is_active,
                'created_date': p.created_date,
            }
            writer.writerow(data)
        
        if email_address:
            email = EmailMessage(
                'Coursebank - Learner Profiles',
                'Attached file of Learner Profiles (as of {})'.format(tnow),
                'no-reply-learner-profiles@coursebank.ph',
                [email_address,],
                )
        email.attach_file(output_file)
        email.send()
