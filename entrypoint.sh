
#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=TaskManager.settings.produccion

echo 'Applying migrations...'
python manage.py wait_for_db --settings=TaskManager.settings.produccion
python manage.py migrate --settings=TaskManager.settings.produccion

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=TaskManager.settings.produccion TaskManager.wsgi:application --bind 0.0.0.0:$PORT
