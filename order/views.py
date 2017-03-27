#coding=utf-8
from django.shortcuts import *
from django.http import HttpResponse
from .forms import *
from order.models import *
import sys
# Create your views here.

def index(request):
    return render(request,'index.html')

def order(request):
    return render(request,'tables.html')

def add_order(request):
    if request.method == "POST":
        or_title = request.POST.get('fo_title')
        or_type = request.POST.get('fo_type')
        or_text = request.POST.get('fo_text')

        u_id = order_user.objects.get(id=1)
        order_info = order_forms(order_type=or_type,order_title=or_title,order_text=or_text,faqi_user=u_id)
        order_info.save()
        return redirect('/order/not/')
    else:
        order_b = add_order_forms()
        return render(request,'order/order_add.html',{'order_b':order_b})

def search(request):
    if 'q' in request.GET:
        message = 'YOU SEARCHE FOR:%r' % request.GET['q']
    else:
        message = '提交为空'
    return HttpResponse(message)
