import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.core.management.base import BaseCommand
from course_modes.models import CourseMode
from opaque_keys.edx.keys import CourseKey
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class Command(BaseCommand):
    help = 'Export enrollment data from Django models to a CSV file and send it via email'

    def add_arguments(self, parser):
        parser.add_argument('-e', '--recipient_email', type=str, help='Recipient email address')

    def handle(self, *args, **options):
        recipient_email = options['recipient_email']

        if not recipient_email:
            self.stderr.write('Recipient email address is required. Please provide it using -e option.')
            return

        # Fetch live courses from Django models
        live_courses = CourseOverview.objects.filter(is_enrollable=True)

        # Prepare the enrollment data
        enrollment_data = []
        for course in live_courses:
            course_key = CourseKey.from_string(course.id)
            audit_count = CourseMode.objects.filter(course_id=course_key, mode_slug='audit').count()
            verified_count = CourseMode.objects.filter(course_id=course_key, mode_slug='verified').count()
            honor_count = CourseMode.objects.filter(course_id=course_key, mode_slug='honor').count()
            enrollment_data.append({
                'Course ID': course.id,
                'Course Name': course.display_name,
                'Audit': audit_count,
                'Verified': verified_count,
                'Honor': honor_count
            })

        # Create a CSV file in-memory
        csv_file_path = 'enrollment_info.csv'
        with open(csv_file_path, 'w', newline='') as f:
            fieldnames = ['Course ID', 'Course Name', 'Audit', 'Verified', 'Honor']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(enrollment_data)

        # Send the email with the CSV attachment
        subject = 'Enrollment Data from Django Models'
        body = 'Please find the attached CSV file containing the enrollment data.'
        sender_email = 'learn@coursebank.ph'  # Replace with the sender email address

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Attach the CSV file to the email
        with open(csv_file_path, 'rb') as file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename={csv_file_path}')
            msg.attach(attachment)

        # Connect to SMTP server and send the email
        smtp_server = 'smtp.sendgrid.net'
        smtp_port = 587 
        smtp_username = 'apikey'
        smtp_password = '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'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        self.stdout.write(self.style.SUCCESS(f'Enrollment data exported and sent to {recipient_email} successfully'))
