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
	"followers": [],
	"following": []
}
```

### Follow Management
`POST /api/accounts/follow/<user_id>/` — Follow a user (requires authentication)
`POST /api/accounts/unfollow/<user_id>/` — Unfollow a user (requires authentication)

**Follow Request:**
`POST /api/accounts/follow/2/`
**Response:**
```json
{
	"success": "You are now following username2"
}
```

**Unfollow Request:**
`POST /api/accounts/unfollow/2/`
**Response:**
```json
{
	"success": "You have unfollowed username2"
}
```

### Feed
`GET /api/feed/` — Get posts from users you follow (requires authentication)

**Feed Response:**
```json
[
	{
		"id": 3,
		"author": "username2",
		"title": "Post from followed user",
		"content": "...",
		"created_at": "2025-08-24T10:00:00Z",
		"updated_at": "2025-08-24T10:00:00Z"
	},
	// ...more posts
]
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

### Likes
`POST /api/posts/{id}/like/` — Like a post (requires authentication)
`POST /api/posts/{id}/unlike/` — Unlike a post (requires authentication)

**Like Post Request:**
`POST /api/posts/1/like/`
**Response:**
```json
{
	"success": "Post liked"
}
```

**Unlike Post Request:**
`POST /api/posts/1/unlike/`
**Response:**
```json
{
	"success": "Post unliked"
}
```

### Notifications
`GET /api/notifications/` — Get notifications for the authenticated user

**Notification Response:**
```json
[
	{
		"id": 1,
		"actor": "username2",
		"verb": "liked your post",
		"target": "My First Post",
		"timestamp": "2025-08-24T10:10:00Z"
	},
	// ...more notifications
]
```

**How to Use:**
- Like a post to notify the post author.
- Unliking a post removes your like (notification remains for history).
- View notifications to see recent interactions (likes, follows, comments).

**Benefits:**
- Users are kept informed of important interactions, increasing engagement.
- Notifications help users track activity and respond to others.

**Testing:**
- Use Postman or automated tests to:
	- Like/unlike posts and verify notifications.
	- View notifications and confirm correct data.
	- Ensure duplicate likes are prevented.

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
- `following`: ManyToMany field (via `related_name`) for users this user follows

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