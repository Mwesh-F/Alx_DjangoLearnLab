# Django Blog Project

## Overview
This project is a comprehensive Django-based blog application designed for learning and practice. It covers essential aspects of Django development, including project setup, user authentication, blog post management, and profile features.

## Features
- User registration, login, and logout
- Profile management (view and update username/email)
- Blog post model (title, content, published date, author)
- Static and template directories for custom styling and layout

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd django_blog
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .venv
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   ```
3. **Install dependencies:**
   ```sh
   pip install django
   ```
4. **Apply migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
6. **Access the app:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Authentication System
- **Registration:** Users can sign up with a username, email, and password.
- **Login/Logout:** Secure login and logout using Django's authentication system.
- **Profile:** Authenticated users can view and update their profile information.

## Directory Structure
- `blog/forms.py`: Custom forms for registration and profile update
- `blog/views.py`: Views for authentication and profile management
- `blog/urls.py`: URL patterns for authentication routes
- `blog/templates/blog/`: HTML templates for login, registration, and profile
- `blog/models.py`: Blog post model
- `blog/static/blog/`: Static files (CSS, JS, images)

## Security
- All forms use CSRF tokens for protection
- Passwords are securely hashed using Django's built-in algorithms

## Testing
- Test registration, login, logout, and profile update by accessing the respective URLs
- Ensure feedback messages appear for errors and confirmations

## Functionality for blog posts

## Features
- **List Posts:** All blog posts are listed at `/posts/`.
- **View Post:** Individual post details are shown at `/posts/<int:pk>/`.
- **Create Post:** Authenticated users can create new posts at `/posts/new/`.
- **Edit Post:** Authors can edit their posts at `/posts/<int:pk>/edit/`.
- **Delete Post:** Authors can delete their posts at `/posts/<int:pk>/delete/`.

## Permissions
- Only authenticated users can create posts.
- Only the author of a post can edit or delete it (enforced with `LoginRequiredMixin` and `UserPassesTestMixin`).
- All users can view the list and details of posts.

## Navigation
- Links are provided in templates for easy navigation between list, detail, edit, and delete views.

## Data Handling
- The post author is automatically set to the logged-in user when creating a post.
- Form validation is handled by Django's `ModelForm`.

## How to Use
1. Log in or register for an account.
2. Go to `/posts/` to view all posts.
3. Use the 'Create New Post' link to add a post.
4. Click a post title to view details.
5. If you are the author, use 'Edit' or 'Delete' links on the detail page.

## Files Updated
- `models.py`: Defines the `Post` model.
- `forms.py`: Adds `PostForm` for post creation and editing.
- `views.py`: Implements class-based views for CRUD operations.
- `urls.py`: Maps URLs to views.
- `templates/blog/`: Contains HTML templates for each operation.

## Security Notes
- Only authors can modify or delete their posts.
- CSRF protection is enabled in all forms.

## Comment System

This Django blog project includes a comment system for blog posts, allowing users to interact and discuss content.

### Features
- Users can view all comments under each blog post.
- Authenticated users can add new comments directly on the post detail page.
- Comment authors can edit or delete their own comments.

### Permissions
- Only authenticated users can add comments.
- Only the author of a comment can edit or delete it.
- All users can view comments.

### How to Use
1. Log in or register for an account.
2. Go to any blog post detail page to view comments.
3. Use the comment form at the bottom of the post to add a new comment.
4. If you are the author, use the 'Edit' or 'Delete' links next to your comment to modify or remove it.

### Code Files
- `models.py`: Defines the `Comment` model.
- `forms.py`: Adds `CommentForm` for comment creation and editing.
- `views.py`: Implements class-based views for comment CRUD operations.
- `urls.py`: Maps URLs to comment views.
- `templates/blog/`: Contains HTML templates for comment display, creation, editing, and deletion.

### Security Notes
- Only comment authors can modify or delete their comments.
- CSRF protection is enabled in all forms.

### Testing
- Test adding, editing, and deleting comments as different users.
- Ensure permissions are enforced and navigation links work.

## Tagging and Search Features

This Django blog project supports tagging and search functionality to help users organize and discover content easily.

### Tagging
- Posts can be tagged with one or more keywords during creation or editing.
- To add tags, enter comma-separated tag names in the tags field of the post form (e.g., `Django, Python, Tutorial`).
- Tags are displayed on the post list and detail pages. Clicking a tag shows all posts with that tag.

### Search
- Use the search bar at the top of the post list or search results page to find posts by title, content, or tag.
- Enter a keyword and click "Search" to view matching posts.
- Search results display posts with the keyword in the title, content, or tags.

### How to Use
1. When creating or editing a post, add tags in the provided field.
2. View tags on each post and click a tag to filter posts by that tag.
3. Use the search bar to find posts by keywords or tags.

### Code Modifications
- `models.py`: Added `Tag` model and many-to-many relationship with `Post`.
- `forms.py`: Updated `PostForm` to support tag input and creation.
- `views.py`: Added search view and tag filtering logic.
- `urls.py`: Added URL patterns for tag filtering and search.
- `templates/blog/`: Updated templates to display tags and search results.

### Security Notes
- Tagging and search features are available to all users.
- CSRF protection is enabled in all forms.

### Testing
- Create and edit posts with tags.
- Click tags to view filtered posts.
- Use the search bar to find posts by title, content, or tag.
- Confirm all features work and integrate smoothly with the blog.
