from django.db import models

from .user import User
from .service import Service
from .request import Request


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)