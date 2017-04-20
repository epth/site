# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class USER(models.Model):
    name=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)
    cellphone=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class POINT(models.Model):
    name = models.CharField(max_length=50)
    map_id = models.IntegerField()
    position_x=models.IntegerField()
    position_y=models.IntegerField()
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class ESSUE(models.Model):
    point_id = models.ForeignKey(POINT, on_delete=models.CASCADE)
    user_id = models.ForeignKey(USER, on_delete=models.CASCADE)
    title=models.CharField(max_length=16)
    instrument = models.CharField(max_length=100)
    isresovled=models.BooleanField(default=False)
    start_date=models.DateTimeField()
    close_date=models.DateTimeField()
    def __str__(self):
       return self.title
