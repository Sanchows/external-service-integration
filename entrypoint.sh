#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
chmod -R 777 staticfiles

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi
exec "$@"