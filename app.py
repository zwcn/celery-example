from celery import Celery

app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//',
    backend='redis://localhost:6379/1',
    include=[
        'tasks.add',
        'tasks.minus',
    ]
)

app.conf.timezone = 'America/New_York'
app.conf.enable_utc = False
