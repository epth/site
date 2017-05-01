# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from .models import DOWNLOAD
import os.path

# Create your views here.
def download(request,download_id=''):
    # do something
    a=DOWNLOAD.objects.get(id=download_id)

    the_file_name=os.path.basename(a.path)             #显示在弹出对话框中的默认的下载文件名    
    filename=a.path                    #要下载的文件路径
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
