from dotenv import load_dotenv
from TaskManager.settings.base import *
from TaskManager.logging import *

import os
env_path = Path(BASE_DIR) / '.env'
load_dotenv(env_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [ 'https://hernandezpalo-taskmanager.up.railway.app', 'hernandezpalo-taskmanager.up.railway.app' , 'https://taskmanager-dev-ctbs.1.us-1.fl0.io']

CSRF_TRUSTED_ORIGINS = ['https://hernandezpalo-taskmanager.up.railway.app', 'https://taskmanager-dev-ctbs.1.us-1.fl0.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME') ,
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        }
    }
