from django.core.management.base import BaseCommand

from account.models import CustomUser


class Command(BaseCommand):
    help = "Command for scheduling sms for every sms type in every org"
    
    def handle(self, *args, **options):
        if not CustomUser.objects.filter(email='admin@admin.com').exists():
            CustomUser.objects.create_superuser('admin@admin.com', 'Pass@123')
