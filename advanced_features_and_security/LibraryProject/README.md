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

## Security Measures Implemented

- **CSRF Protection**: All POST forms utilize `{% csrf_token %}` to prevent Cross-Site Request Forgery.
- **SQL Injection Prevention**: Data access is handled through Django’s ORM, which uses parameterized queries to sanitize user input.
- **Security Headers**: Configured `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF` to harden the application against XSS and clickjacking.
- **Secure Cookies**: Enabled `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` to ensure cookies are only transmitted over HTTPS.

### Content Security Policy (CSP)
We have implemented a basic Content Security Policy to mitigate XSS attacks. 
The policy is set to `default-src 'self'`, which instructs the browser to only 
load content (scripts, styles, etc.) from our own domain. 
This is enforced via a custom middleware that adds the `Content-Security-Policy` 
header to every outgoing HTTP response.