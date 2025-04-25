from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

# Classe herda da class Model
class Community(models.Model):
    """
    Class data
    """
    nome = models.CharField(max_length=100,unique=True,validators=[MinLengthValidator(5)])
    sobre = models.CharField(max_length=256)