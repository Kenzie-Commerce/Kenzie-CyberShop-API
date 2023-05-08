set -o errexit

poetry install --no-dev
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_admin