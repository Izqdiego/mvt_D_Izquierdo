from pyexpat import model
from django.db import models

# Create your models here.

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    f_nac = models.DateTimeField()
    