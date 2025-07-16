from celery.schedules import crontab
from celery_app import app
from tasks import scheduled_scrape

app.conf.beat_schedule = {
    'scrape-every-2-minutes': {
        'task': 'tasks.scheduled_scrape',
        'schedule': crontab(minute='*/2'),  # every 2 minutes
    },
}
app.conf.timezone = 'Asia/Kolkata'
