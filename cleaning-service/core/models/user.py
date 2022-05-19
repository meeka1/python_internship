from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    role = models.CharField(max_length=15)

    def __str__(self):
        return self.fullname