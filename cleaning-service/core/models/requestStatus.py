from django.db import models

STATUSES = {  # Statuses of the order
    ("pending", "Pending"),
    ("completed", "Completed"),
    ("canceled", "Canceled"),
}

class RequestStatus(models.Model):
    status = models.CharField(verbose_name="Order status", max_length=15, choices=STATUSES, null=False)

    def __str__(self):
        return self.status