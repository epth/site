# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import USER,GRADE,KNOWLEDGE

# Register your models here.
admin.site.register(USER)
admin.site.register(GRADE)
admin.site.register(KNOWLEDGE)
