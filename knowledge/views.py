# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import KNOWLEDGE,USER

from django import forms
from django.forms import ModelForm
from ckeditor.fields import RichTextFormField

class Knowledge(ModelForm):
    #title = forms.CharField()
    #content = RichTextFormField()
    class Meta:
     model = KNOWLEDGE
     fields = ('title','content','grade')

# Create your views here.
def index(request,sugar_id=''):
    if request.method == 'POST':
        print request.POST
    all_sugars=KNOWLEDGE.objects.all()
    #print(all_sugars[0].id)
    return render(request,'knowledge/index.html',locals())

def getdetail(request):
    if request.method=='POST':
        a=KNOWLEDGE.objects.get(id=request.POST['sugar_id'])
        b=a.content
        print b
        return HttpResponse(str(b))

def add(request):
    if request.method == "POST":
        f = Knowledge(request.POST)
        if f.is_valid():
            try:
                print '1'
                ck=request.COOKIES.get('username')
                print '2'
                print ck
            except:
                print 'cookie:username does not exist'
                return HttpResponse('尚未登录，请登录')
            if ck!=None:
                try:
                    a=USER.objects.get(name=ck)
                except:
                    print 'user:'+ck+' does not exist!'
                    return HttpResponse('没有此用户')
                newf=KNOWLEDGE.objects.create(user=a,grade=f.cleaned_data['grade'],title=f.cleaned_data['title'],content=f.cleaned_data['content'])
                newf.save()
                return HttpResponse('提交成功')
            else:
                return HttpResponse('尚未登录，请登录')
        else:
            return render(request,"knowledge/add.html",{"error":f.errors,"form":f})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        f = Knowledge()
        return render(request,"knowledge/add.html",{"form":f})
