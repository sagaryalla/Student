from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
