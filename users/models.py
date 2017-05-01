# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class USER(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=16)
    telephone=models.CharField(max_length=50)
    cellphone=models.CharField(max_length=50)
    def __str__(self):
        return self.name

