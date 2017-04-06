#coding=utf-8
from django.shortcuts import *
from django.http import HttpResponse
from order.models import *
from asset.models import *
import sys

def index(request):
    return render(request,'index.html')

def idc_index(request):
    idc_info = j_IDC.objects.all()
    return render(request,'asset/idc_index.html',{'idc_info':idc_info})

def host_index(request):
    return render(request,'host_index.html')

def vm_index(request):
    return render(request,'idc_index.html')

def net_index(request):
    return render(request,'host_index.html')

def docker_index(request):
    return render(request,'idc_index.html')

def pc_index(request):
    return render(request,'host_index.html')
