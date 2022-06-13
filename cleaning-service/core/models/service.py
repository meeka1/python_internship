from django.db import models
from core.models.user import User

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    cost = models.FloatField()
    company = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)