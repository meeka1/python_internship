from django.db import models
from .user import User

ROLE_TYPES = { 
    
    ("client", "Client"), 
    ("company", "Company"),

    }

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    roles_id = models.CharField(max_length=20, choices=ROLE_TYPES)