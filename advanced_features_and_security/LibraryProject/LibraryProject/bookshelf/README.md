# Permissions and Groups Setup

This Django application uses groups and custom permissions to control access to specific views.

## Permissions

Permissions are defined in the `Post` model as follows:
- `can_view`: Allows viewing posts.
- `can_create`: Allows creating new posts.
- `can_edit`: Allows editing existing posts.
- `can_delete`: Allows deleting posts.

## Groups

The following groups are set up with respective permissions:
- `Viewers`: Can view posts only.
- `Editors`: Can create and edit posts.
- `Admins`: Can view, create, edit, and delete posts.

## Usage in Views

Permissions are enforced in views using the `@permission_required` decorator. Users without the required permissions will receive a "Permission Denied" message.
s