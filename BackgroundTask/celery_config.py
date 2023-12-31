from celery import Celery
from django.conf import settings
import os

# set the DJANGO_SETTINGS_MODULE environment variable to BackgroundTask.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BackgroundTask.settings')

# create an instance of the celery class 
app = Celery('Background_app')

#load the configurations accociated with the celery app to prefix  them with CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# make the celery app autmatically find tasks in the installed apps in your django settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#configure the task to execute itself every 60 seconds
app.conf.beat_schedule = {
    'my_periodic_task': {
        'task': 'Background_app.tasks.greet',
        'schedule': 60,  # 60 seconds = 1 minute
    },
}