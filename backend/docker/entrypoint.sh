#!/bin/sh
set -e

echo "Waiting for DB..."

DB_HOST="${DB_HOST:-db}"
DB_PORT="${DB_PORT:-5432}"

# čekaj dok baza ne postane dostupna
until nc -z "$DB_HOST" "$DB_PORT"; do
  echo "DB not ready at ${DB_HOST}:${DB_PORT} - sleeping..."
  sleep 1
done

echo "DB is up!"

# migracije
python manage.py migrate --noinput

# static fajlovi (WhiteNoise)
python manage.py collectstatic --noinput || true

# pokretanje aplikacije (production)
exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}