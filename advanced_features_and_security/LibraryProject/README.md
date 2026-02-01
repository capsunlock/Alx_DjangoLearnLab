# Permissions and Groups Setup

## Custom Permissions
Custom permissions are defined in the `Book` model within `bookshelf/models.py`:
- `can_view`: Allows users to view book details.
- `can_create`: Allows users to add new books.
- `can_edit`: Allows users to modify existing books.
- `can_delete`: Allows users to remove books from the library.

## Groups Configuration
The following groups should be created via the Django Admin panel:
1. **Editors**: Should be assigned `can_create` and `can_edit`.
2. **Viewers**: Should be assigned `can_view`.
3. **Admins**: Should be assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).