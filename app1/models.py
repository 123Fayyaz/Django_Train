from django.db import models

# Create your models here.

class Train_Details(models.Model):
    num=models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    departure_place = models.CharField(max_length=200)
    destination_place = models.CharField(max_length=200)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()






















