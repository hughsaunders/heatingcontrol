from django.db import models

# Create your models here.

class Temperature(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField()
    probe = models.ForeignKey('Probe')

class Probe(models.Model):
    name = models.TextField()
    location = models.TextField()
