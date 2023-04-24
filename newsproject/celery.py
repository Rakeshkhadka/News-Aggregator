import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsproject.settings')

app = Celery('newsproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'scrape_ekantipur_120s':{
        'task':'scraper.tasks.scrape_ekantipur',
        'schedule': 120.0
    },
    'scrape_nagarik_120s':{
        'task':'scraper.tasks.scrape_nagarik',
        'schedule': 120.0
    }
}


# Load task modules from all registered Django apps.
app.autodiscover_tasks()