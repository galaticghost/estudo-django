from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

# Create your models here.

class XinaModel(models.Model):
    title = models.CharField(max_length=50)

class User(AbstractUser):
    pass