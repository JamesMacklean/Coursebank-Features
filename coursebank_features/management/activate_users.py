from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Activate inactive users from July 2023 until today.'

    def handle(self, *args, **kwargs):
        # Get the date from July 2023
        july_2023 = timezone.datetime(2023, 7, 1, tzinfo=timezone.utc)
        
        # Get the current date
        now = timezone.now()

        # Get inactive users from June 2023 until today
        inactive_users = User.objects.filter(is_active=False, date_joined__gte=july_2023, date_joined__lte=now)

        # Activate inactive users
        count = 0
        for user in inactive_users:
            count = count + 1
            user.is_active = True
            user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully activated {count} inactive users.'))
