#!/bin/sh
set -e

echo "Waiting for DB..."
while ! nc -z db 5432; do
  sleep 0.5
done

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Starting Django..."
exec python manage.py runserver 0.0.0.0:8000
