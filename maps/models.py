# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import USER

# Create your models here.

#class USER(models.Model):
#    name=models.CharField(max_length=50)
#    telephone=models.CharField(max_length=50)
#    cellphone=models.CharField(max_length=50)
#    def __str__(self):
#        return self.name


class POINT(models.Model):
    name = models.CharField(max_length=50)
    map_id = models.IntegerField()
    position_x=models.IntegerField()
    position_y=models.IntegerField()
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    computername=models.CharField(max_length=50)
    ip=models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    status=models.CharField(max_length=50,default='Idle')
    message=models.CharField(max_length=100,default='Idle')
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



class ESSUE(models.Model):
    point = models.ForeignKey(POINT, on_delete=models.CASCADE)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    title=models.CharField(max_length=16)
    instrument = models.CharField(max_length=100)
    isresovled=models.BooleanField(default=False)
    start_date=models.DateTimeField()
    close_date=models.DateTimeField()
    def __str__(self):
       return self.title
