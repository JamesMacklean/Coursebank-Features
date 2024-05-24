from django.core.management.base import BaseCommand, CommandError
from student.models import CourseEnrollment, CourseEnrollmentAllowed
from opaque_keys.edx.keys import CourseKey
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Re-enroll a user in a specified course'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the learner to re-enroll')
        parser.add_argument('course_id', type=str, help='Course ID to re-enroll the learner in')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        course_id = kwargs['course_id']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError('User "{}" does not exist'.format(username))

        course_key = CourseKey.from_string(course_id)

        # Check if user is already enrolled
        enrollment = CourseEnrollment.objects.filter(user=user, course_id=course_key).first()
        
        if enrollment:
            if enrollment.is_active:
                self.stdout.write(self.style.WARNING('User "{}" is already enrolled in course "{}"'.format(username, course_id)))
            else:
                # Reactivate the enrollment
                enrollment.is_active = True
                enrollment.save()
                self.stdout.write(self.style.SUCCESS('User "{}" has been re-enrolled in course "{}"'.format(username, course_id)))
        else:
            # Create a new enrollment
            CourseEnrollmentAllowed.objects.get_or_create(user=user, course_id=course_key)
            CourseEnrollment.objects.create(user=user, course_id=course_key, is_active=True)
            self.stdout.write(self.style.SUCCESS('User "{}" has been enrolled in course "{}"'.format(username, course_id)))
