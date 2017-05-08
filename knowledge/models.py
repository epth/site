# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ckeditor.fields import RichTextField

from users.models import USER

# Create your models here.

#class USER(models.Model):
#    name=models.CharField(max_length=50)
#    telephone=models.CharField(max_length=50)
#    cellphone=models.CharField(max_length=50)
#    def __str__(self):
#        return self.name


class GRADE(models.Model):
    name = models.CharField(max_length=50)
    mark=models.IntegerField()
    image_filepath=models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class KNOWLEDGE(models.Model):
    grade = models.ForeignKey(GRADE, on_delete=models.CASCADE)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    title=models.CharField(max_length=16)
    content=RichTextField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.title
