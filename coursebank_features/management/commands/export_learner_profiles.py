import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from io import StringIO

class Command(BaseCommand):
    help = 'Export data from Django User model to a CSV file and send it via email'

    def add_arguments(self, parser):
        parser.add_argument('-e', '--recipient_email', type=str, help='Recipient email address')

    def handle(self, *args, **options):
        recipient_email = options['recipient_email']

        if not recipient_email:
            self.stderr.write('Recipient email address is required. Please provide it using -e option.')
            return

        queryset = User.objects.all()

        # Prepare the CSV data as a string
        csv_data = StringIO()
        writer = csv.writer(csv_data)
        writer.writerow(['id', 'name', 'username', 'date_joined', 'is_active'])

        for user in queryset:
            writer.writerow([user.id, user.get_full_name(), user.username, user.date_joined, user.is_active])

        # Create the email message with CSV attachment
        subject = 'Exported Coursebank Learner Profiles'
        body = 'Please find the attached CSV file containing the learner profiles'
        sender_email = 'no-reply-coursebank-learner-profiles@example.com'

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=sender_email,
            to=[recipient_email],
        )

        email.attach('learner_profiles.csv', csv_data.getvalue(), 'text/csv')

        # Send the email
        email.send()

        self.stdout.write(self.style.SUCCESS(f'Learner profiles data exported and sent to {recipient_email} successfully'))
