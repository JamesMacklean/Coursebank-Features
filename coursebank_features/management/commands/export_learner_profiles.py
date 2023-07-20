import csv
import os
from pprint import pformat

import logging
log = logging.getLogger(__name__)

from django.core.management.base import BaseCommand, CommandError

from coursebank_features.utils import export_learner_profiles


class Command(BaseCommand):
    help = 'Exports learner profiles.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-e',
            '--email',
            type=str,
            help='set email to send to',
        )

    def handle(self, *args, **options):
        email_address = options.get('email', None)

        try:
            export_learner_profiles(email_address=email_address)
        except Exception as e:
            raise CommandError("Error in exporting learner profiles: {}".format(str(e)))
        else:
            self.stdout.write(self.style.SUCCESS("Successfully exported learner profiles."))
