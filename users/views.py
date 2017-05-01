# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django import forms
from django.forms import ModelForm
from ckeditor.fields import RichTextFormField
from .models import USER

# Create your views here.
def index(request):
    return render(request,'users/index.html',locals())

def login(request):
    if request.method=='POST':
        if request.POST.get('username') == None:
            return render(request,'users/login.html',locals())
        else:
            try:
                a=USER.objects.get(name=request.POST.get('username'),password=request.POST.get('password'))
            except:
                return HttpResponse('用户名或密码错误')
            b=HttpResponse('success')
            b.set_cookie('username',a,3600)
            return b


def register(request):
    if request.method=='POST':
        a=USER.objects.create(name=request.POST.get('username'),password=request.POST.get('password'))
        a.save()
        return HttpResponse('success')
