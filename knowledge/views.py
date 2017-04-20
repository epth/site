# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import KNOWLEDGE

# Create your views here.
def index(request,sugar_id=''):
    if request.method == 'POST':
        print request.POST
    all_sugars=KNOWLEDGE.objects.all()
    #print(all_sugars[0].id)
    return render(request,'knowledge/index.html',locals())

def add(request):
    a = request.POST['a']
    b = request.POST['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def getdetail(request):
    if request.method=='POST':
        a=KNOWLEDGE.objects.get(id=request.POST['sugar_id'])
        b=a.instrument
        return HttpResponse(str(b))

#def sugar_detail(request,sugar_id):
#    return render(request)
