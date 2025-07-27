from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Set up user groups and assign custom permissions for the Book model.'

    def handle(self, *args, **options):
        # Define group names and their permissions
        group_permissions = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, perms in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created group: {group_name}'))
            else:
                self.stdout.write(f'Group already exists: {group_name}')

            # Clear existing permissions
            group.permissions.clear()

            # Assign permissions
            for perm_codename in perms:
                try:
                    perm = Permission.objects.get(codename=perm_codename, content_type__app_label='bookshelf')
                    group.permissions.add(perm)
                    self.stdout.write(self.style.SUCCESS(f'  Assigned permission: {perm_codename}'))
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'  Permission not found: {perm_codename}'))

        self.stdout.write(self.style.SUCCESS('Groups and permissions setup complete.')) 