from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100,)
    #genre = models.CharField(max_length=100,)
    description = models.TextField(max_length=1000, blank=False)
    year = models.PositiveIntegerField(blank=True, null=True)
    #score = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])