# Notes Backend App (Django)

This is a simple **note-taking backend application** built with Django that supports user authentication and CRUD operations for notes.

---

## 🚀 How to Install and Run Locally

### 📦 Prerequisites
- Python 3.8+
- pip (Python package manager)
- MySQL (or SQLite if used)
- Git

### 🔧 Setup Steps

1. **Clone the repository**
   ```bash
   git clone <https://github.com/KIRUBAKARAN9840/i2_global.git>
   cd i2_global


2.Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


3.Install dependencies
pip install -r requirements.txt

4.Set up environment variables

Create a .env file and add:

SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=notesdb
DB_USER=your-mysql-username
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306


5.Apply migrations
python manage.py makemigrations
python manage.py migrate

6.admin panel
python manage.py createsuperuser
(create login and password)


at last............run the server
python manage.py runserver
