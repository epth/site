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


class GRADE(models.Model):
    name = models.CharField(max_length=50)
    mark=models.IntegerField()
    image_filepath=models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class KNOWLEDGE(models.Model):
    grade_id = models.ForeignKey(GRADE, on_delete=models.CASCADE)
    user_id = models.ForeignKey(USER, on_delete=models.CASCADE)
    title=models.CharField(max_length=16)
    instrument = models.CharField(max_length=100)
    create_time=models.DateTimeField()
    lastedit_time=models.DateTimeField()
    def __str__(self):
       return self.title
