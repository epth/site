# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import POINT
import datetime
import time
import json

# Create your views here.
def index(request):
    a=[]
    points=POINT.objects.all()
    i=0
    for c in points:
        d={}
        d['name']=c.name
        d['x']=c.position_x
        d['y']=c.position_y
        d['computername']=c.computername
        d['user']=str(c.user)
        d['status']=c.status
        d['message']=c.message
        d['ip']=c.ip
        d['id']=i
        a.append(d)
        i+=1
    b=json.dumps(a,ensure_ascii=False)
    return render(request,'maps/index.html',locals())
def points(request):
    return render(request,'maps/events-click-getcoordinates.html')
def task(request):
    while(True):
        a=POINT.objects.get(update_time__gt=(datetime.datetime.now()-datetime.timedelta(hours=2)))
        print a
        time.sleep(5)
