from  celery  import shared_task
from core.models.user  import User
from django.utils.crypto import get_random_string
from  random  import  randint


import string
from  random  import  randint, choice

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