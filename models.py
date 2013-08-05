from django.db import models

class DoorEvent(models.Model):
    lastdatetime = models.DateTimeField('last update') 
    kount = models.SmallIntegerField('kitty kount')
    direction = models.CharField('direction', max_length = 10)
