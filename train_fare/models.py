from django.db import models

# Create your models here.
class fare(models.Model):
    TrainNum=models.PositiveIntegerField()
    OrgCity = models.CharField(max_length=200)
    DesCity = models.CharField(max_length=200)
    TrainFare = models.PositiveIntegerField()
