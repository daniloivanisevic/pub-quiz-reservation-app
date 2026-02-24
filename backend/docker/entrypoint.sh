
set -e

echo "Waiting for DB..."

DB_HOST="${DB_HOST:-db}"
DB_PORT="${DB_PORT:-5432}"


until nc -z "$DB_HOST" "$DB_PORT"; do
  echo "DB not ready at ${DB_HOST}:${DB_PORT} - sleeping..."
  sleep 1
done

echo "DB is up!"


python manage.py migrate --noinput


python manage.py collectstatic --noinput || true


exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}