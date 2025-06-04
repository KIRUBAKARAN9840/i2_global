# Notes Backend (Django)

A simple Django REST API for user authentication and note management.

=====================
🚀 HOW TO INSTALL & RUN LOCALLY
=====================

1. Clone the repository
   git clone https://github.com/KIRUBAKARAN9840/i2_global.git
   cd i2_global

2. Create a virtual environment
   python -m venv venv
   venv\Scripts\activate   (on Windows)

3. Install dependencies
   pip install -r requirements.txt

4. Create a `.env` file in the root folder with the following:
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=your-database-name
   DB_USER=your-username
   DB_PASSWORD=your-password
   DB_HOST=localhost
   DB_PORT=3306

5. Run migrations
   python manage.py makemigrations
   python manage.py migrate

6. Create superuser
   python manage.py createsuperuser

7. Run the development server
   python manage.py runserver

Visit http://127.0.0.1:8000/ to check the API is running

=====================
💡 DESIGN DECISIONS & TRADE-OFFS
=====================

- Used Django REST Framework for quick development and reliable API structure.
- Used MySQL as the primary database for production use.
- JWT (via SimpleJWT) is used for token-based authentication.
- Kept a single app (notesapp) for both user and notes logic to simplify structure.
- Project is made docker-free to keep local testing and deployment simple.

=====================
📎 EXTERNAL RESOURCES USED
=====================

All logic and code are written from scratch. Below resources used for guidance only:

- Django Official Docs: https://docs.djangoproject.com/
- Simple JWT Docs: https://django-rest-framework-simplejwt.readthedocs.io/

=====================
📂 PROJECT STRUCTURE
=====================

notes-backend/
─ manage.py
─ .env
─ requirements.txt
─ README.md
─ notesbackend/      (settings, wsgi, urls)
─ notesapp/          (models, views, urls, serializers, admin)

=====================
👤 AUTHOR
=====================

M. Kirubakaran
