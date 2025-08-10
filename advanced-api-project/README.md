# Advanced API Project - Book CRUD Endpoints

This project demonstrates advanced API development using Django REST Framework (DRF), focusing on custom and generic views, permissions, and robust endpoint design.

## Book Endpoints

- **List all books**: `GET /api/books/`
- **Retrieve a book**: `GET /api/books/<id>/`
- **Create a book**: `POST /api/books/create/` (Authenticated users only)
- **Update a book**: `PUT/PATCH /api/books/<id>/update/` (Authenticated users only)
- **Delete a book**: `DELETE /api/books/<id>/delete/` (Authenticated users only)

## Permissions
- List and retrieve endpoints are open to all users (read-only for unauthenticated users).
- Create, update, and delete endpoints require authentication.

## Customizations
- Book creation and update validate that `publication_year` is not in the future.
- Permissions are enforced using DRF's `IsAuthenticated` and `AllowAny` classes.

## How to Test
- Use Postman, curl, or any API client to interact with the endpoints.
- Attempt to create, update, or delete a book as an unauthenticated user to confirm permission enforcement.
- Authenticated users can perform all CRUD operations.

## Code Structure
- Views: `api/views.py` (uses DRF generic views)
- URLs: `api/urls.py` (routes endpoints to views)
- Serializers: `api/serializers.py` (handles validation and serialization)
- Models: `api/models.py` (Book and Author models)

## Extending Functionality
- Add custom permission classes or filters as needed in the views.
- See code comments for further customization points.
