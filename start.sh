python manage.py migrate
python manage.py collectstatic --noinput
gunicorn pro_deploy.wsgi:application