## Authentication and Permissions
This API implements **Token-based Authentication**. 
- **Endpoint**: `/api-token-auth/` (POST username and password to receive a token).
- **Usage**: Include the header `Authorization: Token <your_token>` in all requests.
- **Permissions**: The `BookViewSet` is restricted using `IsAuthenticated`, ensuring only logged-in users with a valid token can access or modify book data.