from django.db import models
from core.models.user import User
from core.models.requestStatus import RequestStatus
from core.models.service import Service

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total_area = models.FloatField()
    total_cost = models.OneToOneField(Service, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status_id = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
