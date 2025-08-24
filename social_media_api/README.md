# Social Media API

This project is a Django REST Framework-based Social Media API. It provides user authentication, profile management, and is ready for further social media features (posts, comments, follows, notifications, likes).

## Project Structure

```
social_media_api/
├── accounts/                # User authentication app
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py            # Custom user model
│   ├── serializers.py       # User serializer
│   ├── tests.py
│   ├── urls.py              # API routes for accounts
│   └── views.py             # Registration, login, profile views
├── manage.py
├── README.md
├── social_media_api/
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL routing
│   └── ...
└── venv/                    # Virtual environment
```

## Setup Instructions

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:
	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate
	```
3. Install dependencies:
	```powershell
	pip install django djangorestframework djangorestframework-simplejwt
	```
4. Apply migrations:
	```powershell
	python manage.py makemigrations
	python manage.py migrate
	```
5. Start the development server:
	```powershell
	python manage.py runserver
	```


## API Endpoints

### Registration
`POST /api/accounts/register/`
**Request Body:**
```json
{
	"username": "your_username",
	"email": "your_email@example.com",
	"password": "your_password"
}
```
**Response:**
```json
{
	"token": "<auth_token>"
}
```

### Login
`POST /api/accounts/login/`
**Request Body:**
```json
{
	"username": "your_username",
	"password": "your_password"
}
```
**Response:**
```json
{
	"token": "<auth_token>"
}
```

### User Profile
`GET /api/accounts/profile/` (Requires authentication)
`PUT /api/accounts/profile/` (Requires authentication)
**Request Body (PUT):**
```json
{
	"bio": "New bio",
	"profile_picture": "<image_url>"
}
```
**Response:**
```json
{
	"id": 1,
	"username": "your_username",
	"email": "your_email@example.com",
	"bio": "New bio",
	"profile_picture": "<image_url>",
	"followers": []
}
```

### Posts
`GET /api/posts/` — List posts (supports pagination and search)
`POST /api/posts/` — Create a post (requires authentication)
`GET /api/posts/{id}/` — Retrieve a post
`PUT /api/posts/{id}/` — Update your own post
`DELETE /api/posts/{id}/` — Delete your own post

**Create Post Request:**
```json
{
	"title": "My First Post",
	"content": "This is the content of my post."
}
```
**Response:**
```json
{
	"id": 1,
	"author": "your_username",
	"title": "My First Post",
	"content": "This is the content of my post.",
	"created_at": "2025-08-24T10:00:00Z",
	"updated_at": "2025-08-24T10:00:00Z"
}
```

**List Posts (with pagination and search):**
`GET /api/posts/?page=1&page_size=10&search=First`

### Comments
`GET /api/comments/` — List comments (supports pagination)
`POST /api/comments/` — Create a comment (requires authentication)
`GET /api/comments/{id}/` — Retrieve a comment
`PUT /api/comments/{id}/` — Update your own comment
`DELETE /api/comments/{id}/` — Delete your own comment

**Create Comment Request:**
```json
{
	"post": 1,
	"content": "Nice post!"
}
```
**Response:**
```json
{
	"id": 1,
	"post": 1,
	"author": "your_username",
	"content": "Nice post!",
	"created_at": "2025-08-24T10:05:00Z",
	"updated_at": "2025-08-24T10:05:00Z"
}
```

**List Comments (with pagination):**
`GET /api/comments/?page=1&page_size=10`

## User Model

Custom user model extends Django's AbstractUser and includes:
- `bio`: Text field for user bio
- `profile_picture`: Image field for profile picture
- `followers`: ManyToMany field for user followers

## Testing

Use Postman, Insomnia, or cURL to test registration, login, and profile endpoints. Ensure tokens are generated and returned correctly.

## Next Steps

- Implement posts, comments, follows, notifications, and likes features.
- Deploy the API to a production environment.

## License

MIT

## Project Setup

1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:
	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate
	```
3. Install dependencies:
	```powershell
	pip install django djangorestframework djangorestframework-simplejwt
	```
4. Apply migrations:
	```powershell
	python manage.py makemigrations
	python manage.py migrate
	```
5. Start the development server:
	```powershell
	python manage.py runserver
	```

## User Registration & Authentication

### Register a User
POST `/api/accounts/register/`
Body (JSON):
```
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
```
Returns: Auth token on success.

### Login
POST `/api/accounts/login/`
Body (JSON):
```
{
  "username": "your_username",
  "password": "your_password"
}
```
Returns: Auth token on success.

### User Profile
GET/PUT `/api/accounts/profile/` (Requires authentication)

## User Model Overview

Custom user model extends Django's AbstractUser and includes:
- `bio`: Text field for user bio
- `profile_picture`: Image field for profile picture
- `followers`: ManyToMany field for user followers

## Notes
- All configuration files and migrations are included in the repository.
- Use tools like Postman to test registration and login endpoints.