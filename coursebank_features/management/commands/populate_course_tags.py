# IMPORTANT NOTE!
# CREATE a csv file with the corresponding columns:
# course, primary topic, skills, subtopics, organization

import os
import csv
import logging

from django.core.management.base import BaseCommand, CommandError
from coursebank_features.models import *

log = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate CourseTag model with data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        if not os.path.exists(csv_file):
            raise CommandError(f'"{csv_file}" does not exist')

        successful_count, failed_count = 0, 0
        
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    primary_topic, _ = PrimaryTopic.objects.get_or_create(name=row['primary topic'])

                    course_tag = CourseTag.objects.create(course=row['course'], primary_topic=primary_topic)

                    for subtopic_name in row['subtopics'].split(','):
                        subtopic, _ = SubTopic.objects.get_or_create(name=subtopic_name.strip())
                        course_tag.subtopic.add(subtopic)

                    for skill_name in row['skills'].split(','):
                        skill, _ = Skill.objects.get_or_create(name=skill_name.strip())
                        course_tag.skills.add(skill)

                    for org_name in row['organization'].split(','):
                        org, _ = Organization.objects.get_or_create(name=org_name.strip())
                        course_tag.organization.add(org)

                    successful_count += 1
                except Exception as e:
                    log.exception(f'Error populating CourseTag: {e}')
                    failed_count += 1

        total_count = successful_count + failed_count
        
        if failed_count:
            msg = f'Completed populating Course Tags. {failed_count} courses of {total_count} courses failed.'
            log.error(msg)
            self.stdout.write(msg)
        else:
            msg = f'Successfully populated {total_count} courses.'
            log.info(msg)
            self.stdout.write(msg)
