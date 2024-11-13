from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Define the groups and their permissions
        group_permissions = {
            'Editors': ['can_create', 'can_edit'],
            'Viewers': ['can_view'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        # Get the model (e.g., Post)
        post_content_type = apps.get_model('your_app', 'Post')._meta.default_related_name

        # Create groups and assign permissions
        for group_name, permissions in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.get(codename=perm, content_type__model=post_content_type)
                group.permissions.add(permission)

            self.stdout.write(f"Group '{group_name}' created with permissions: {permissions}")
