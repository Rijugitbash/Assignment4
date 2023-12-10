# Vendor Management System

# Vendor Management System

## Installation

1. Create and activate a virtual environment.
2. Install requirements: `pip install -r requirements.txt`.
3. Set up the database in `settings.py`.

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
