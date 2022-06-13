from django.db import models
from core.models.user import User
from core.models.service import Service
from core.models.order import Order

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)