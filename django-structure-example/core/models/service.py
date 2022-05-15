from django.db import models
from .user import User


class Service(models.Model):
    # id, name, cost, company, user_id (fk)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    cost = models.FloatField()
    company = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.company
