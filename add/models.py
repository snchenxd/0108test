from django.db import models

# Create your models here
class addDjango2(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=20)
    height = models.CharField(max_length=40)
    sex = models.CharField(max_length=20)

