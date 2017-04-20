# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def download(request):
    # do something

    the_file_name='11.png'             #显示在弹出对话框中的默认的下载文件名    
    filename='media/uploads/11.png'    #要下载的文件路径
    response=StreamingHttpResponse(readFile(filename))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{0}"'.format(the_file_name)
    return response

def readFile(filename,chunk_size=512):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break
