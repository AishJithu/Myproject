from django.db import models

# Create your models here.
class Movies (models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()

class Employee (models.Model):
    name=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    age=models.IntegerField(null=False)
    department=models.CharField(max_length=255)