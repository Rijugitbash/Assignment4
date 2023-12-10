# Vendor Management System

## Installation Process

1. Create a virtual environment.``python -m venv .venv``
2. Activate the virtual environment.``.venv/Script/activate``(windows) || ``source .venv/bin/activate``(Linax)
3. Install requirements using `pip install -r requirements.txt`.
4. Attach the default database with data provided in the project, or set up your own database.

   ```python
   # settings.py
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "mydatabase",
           "USER": "mydatabaseuser",
           "PASSWORD": "mypassword",
           "HOST": "127.0.0.1",
           "PORT": "5432",
       }
   }
5. Create migration files with ``python manage.py makemigrations``.
6. Apply migrations to create tables in the database with ``python manage.py migrate``.
7. Run the project with ``python manage.py runserver``.

#### Attached the  api endpoint documentation in project
