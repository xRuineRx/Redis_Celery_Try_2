import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery_Redis_Try.settings')

app = Celery('mcdonaldsCeleryRedis')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
