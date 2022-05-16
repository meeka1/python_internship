from django.db import models

from .user import User
from .service import Service
from .request import Request

RATINGS = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField(null=True, blank=True, choices=RATINGS)
    feedback = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE, blank=True, null=True)
