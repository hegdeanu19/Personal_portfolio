from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=255)
    date=models.DateField()
  

