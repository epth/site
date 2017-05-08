# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from download.models import DOWNLOAD

# Create your views here.
def index(request):
    all_sugars=DOWNLOAD.objects.all()
    return render(request,'apps/index.html',locals())
