from django.db import models

class LastUpdate(models.Model):
    lastdatetime = models.DateTimeField('last update') 
