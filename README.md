# Django Blog App

## 📌 Overview
This is a simple **Django Blog App** where users can **create, read, update, and delete blog posts**. Users can **register, log in, and log out**, and only authenticated users can create or edit their own posts.

## 🚀 Features
- ✅ **User Authentication** (Register, Login, Logout)
- ✅ **Create, Read, Update, Delete (CRUD) Blog Posts**
- ✅ **Restrict Post Editing** to Post Authors Only
- ✅ **Navigation Bar** with Links to All Pages
- ✅ **CSRF Protection** for Forms

## 🛠️ Technologies Used
- **Django** (Backend)
- **SQLite** (Default Database)
- **HTML, CSS** (Frontend)
- **Bootstrap** (For Styling, optional)

## 📂 Project Structure
```
blog_app/
│── blog/                # Main app
│   ├── migrations/      # Database migrations
│   ├── static/          # Static files (CSS, JS, Images)
│   ├── templates/       # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py         # Forms for posts
│   ├── models.py        # Database models
│   ├── tests.py
│   ├── urls.py          # URL routes
│   ├── views.py         # Views (business logic)
│── blog_project/        # Django project settings
│   ├── __init__.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # Project-wide URL configuration
│   ├── wsgi.py
│── db.sqlite3           # Database file
│── manage.py            # Django management script
│── README.md            # Project documentation
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/abdurrahman310303/blog-app-django.git
cd django-blog-django
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
python install  .../

### 4️⃣ Apply Migrations & Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser  # Follow the prompts
```

### 5️⃣ Run the Server
```bash
python manage.py runserver
```
Visit **`http://127.0.0.1:8000/`** in your browser.

## 📝 Usage
- **Register/Login**: Users can register and log in.
- **Create Post**: Logged-in users can create blog posts.
- **Edit Post**: Only the author can update their posts.
- **Logout**: Users can log out.

## 📜 Routes (URLs)
| Route                  | Description                  |
|------------------------|------------------------------|
| `/`                    | Home page (list of posts)    |
| `/register/`           | User registration page       |
| `/logout/`             | Logout the user             |
| `/create/`             | Create a new blog post      |
| `/post/<post_id>/`     | View a single post          |
| `/post/update/<post_id>/` | Update a post (author only) |

## 👤 Author
**Your Name**  
[GitHub](https://github.com/abdurrahman310303) | [LinkedIn](https://linkedin.com/in/abdur-rahman-5b6907239)  

## 📜 License
This project is licensed under the MIT License.

