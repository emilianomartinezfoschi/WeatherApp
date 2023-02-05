from django.db import models

# Create your models here.
class History(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    temperature = models.DecimalField(null=True, decimal_places=1, max_digits=4)
    thermal_sensation = models.DecimalField(null=True, decimal_places=1, max_digits=4)    
    humidity = models.CharField(max_length=200)
    cloud = models.DecimalField(null=True, decimal_places=1, max_digits=4)
    uv = models.DecimalField(null=True, decimal_places=1, max_digits=4)
    date = models.CharField(max_length=200)