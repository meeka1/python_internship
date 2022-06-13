from  celery  import shared_task
from core.models.user  import User
from django.utils.crypto import get_random_string
from  random  import  randint
import string
from  random  import  randint, choice

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings.settings')
app = Celery('final_project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

@shared_task
def create_user(total):
    for i in range(total):
        fullname = 'user_{}'.format(get_random_string(20, string.ascii_letters))
        email = '{}@example.com'.format(fullname)
        phone = random_with_N_digits(7)
        role = choice(["client", "company"])
        User.objects.create(fullname=fullname, email=email, phone=phone, role=role)
    return '{} random users created with success!'.format(total)