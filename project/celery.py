import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery("project")
app.config.from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def add_num():
    return



