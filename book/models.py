from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=30)
    number=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    date= models.CharField(max_length=30)


