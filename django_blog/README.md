📝 Project Documentation: Django Blog Lab
🚀 Overview
A fully functional blog application built with Django, supporting full CRUD (Create, Read, Update, Delete) operations, user authentication, and author-based permission controls.

🛠 Features & Usage
1. Post Management (CRUD)
Create: Logged-in users can create new posts via /posts/new/.

Read: * List View: The home page (/) displays all recent posts with snippets.

Detail View: Clicking a title (/posts/<id>/) shows the full content.

Update: Authors can edit their posts via /posts/<id>/update/.

Delete: Authors can remove their posts via /posts/<id>/delete/. A confirmation page is required to prevent accidental deletion.

2. User Authentication
Login/Logout: Users must be logged in to create or modify content.

Registration: New users can sign up to become authors.

3. Security & Permissions
We implemented strict data handling to ensure site integrity:

LoginRequiredMixin: Prevents anonymous users from accessing create, update, or delete URLs.

UserPassesTestMixin: Ensures that only the original author of a post can update or delete it. If a user tries to edit someone else's post, they receive a 403 Forbidden error.

🏗 Data Handling & Architecture
The Post Model
The core data structure in models.py handles:

Automatic Dating: Uses auto_now_add to timestamp posts upon creation.

Relational Mapping: Links posts to the User model via a ForeignKey.

Dynamic Routing: The get_absolute_url() method ensures that Django always knows exactly where a post's detail page lives.

URL Structure

URL Pattern,View,Purpose
/,PostListView,Home page list of all posts
/posts/<int:pk>/,PostDetailView,Individual post details
/posts/new/,PostCreateView,Form to create a new post
/posts/<int:pk>/update/,PostUpdateView,Form to edit an existing post
/posts/<int:pk>/delete/,PostDeleteView,Confirmation to remove a post

🖥 Technical Requirements
Framework: Django 6.0.2

Language: Python 3.14.2

Database: SQLite (Development)

💡 Special Notes
Truncation: Post snippets on the home page are limited to 30 words using Django's truncatewords filter for a cleaner UI.

Safety: The success_url for deletions is mapped to the home page using reverse_lazy to avoid circular import/loading issues.