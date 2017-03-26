#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from order.models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def order(request):
    return render(request,'tables.html')

def add(request):
    return render(request,'order/order_add.html')

def search(request):
    if 'q' in request.GET:
        message = 'YOU SEARCHE FOR:%r' % request.GET['q']
    else:
        message = '提交为空'
    return HttpResponse(message)
