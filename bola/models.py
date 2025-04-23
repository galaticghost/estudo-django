from django.db import models
# Create your models here.

# Classe herda da class Model
class Community(models.Model):
    """
    Class data
    """
    nome = models.CharField(max_length=100,unique=True)
    sobre = models.CharField(max_length=256)