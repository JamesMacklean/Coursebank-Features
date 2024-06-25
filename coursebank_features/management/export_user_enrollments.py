import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from your_app.models import Course, Enrollment, Certificate  # Adjust the import as per your models

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

        # Prepare the CSV data as a list of dictionaries
        csv_data = []
        for user in queryset:
            # Get user's courses and certificate status
            enrollments = Enrollment.objects.filter(user=user).select_related('course')
            courses = [{'course_name': enrollment.course.name,
                        'has_certificate': Certificate.objects.filter(user=user, course=enrollment.course).exists()}
                       for enrollment in enrollments]
            
            csv_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'date_joined': user.date_joined,
                'is_active': user.is_active,
                'courses': courses
            })

        # Create a CSV file in-memory
        csv_file_path = 'exported_data.csv'
        with open(csv_file_path, 'w', newline='') as f:
            fieldnames = ['id', 'username', 'email', 'date_joined', 'is_active', 'courses']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for data in csv_data:
                # Convert the courses list to a string representation
                data['courses'] = ', '.join([f"{course['course_name']} (Certificate: {course['has_certificate']})" for course in data['courses']])
                writer.writerow(data)

        # Send the email with the CSV attachment
        subject = 'Exported Data from Django User Model'
        body = 'Please find the attached CSV file containing the data.'
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
        smtp_password = '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'  # Replace with your SMTP password

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        self.stdout.write(self.style.SUCCESS(f'Data exported and sent to {recipient_email} successfully'))
