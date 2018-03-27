# prc
Python + Redis + Celery

Source code for https://code.tutsplus.com/tutorials/using-celery-with-django-for-background-task-processing--cms-28732

This project was compile and tested in macOS Sierra Python 2.7.10

Minor modifications:
celery.py --> celeryapp.py

Install redis:
brew install redis
redis-cli ping
redis-server
pip install redis

Install celery
pip install -U celery
celery worker -A quick_publisher --loglevel=debug --concurrency=4 --app=quick_publisher.celeryapp:app

The right belongs to  George-Bogdan Ivanov as the owner of the post