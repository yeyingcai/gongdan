#coding=utf-8
from django.shortcuts import *
from django.http import HttpResponse
from .forms import *
from order.models import *
import sys
from django.contrib import auth
# Create your views here.

def login_view(request):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username=username, password=password)
  if user is not None and user.is_active:
    # Correct password, and the user is marked "active"
    auth.login(request, user)
    # Redirect to a success page.
    return HttpResponseRedirect("/order/")
  else:
    # Show an error page
    return HttpResponseRedirect("/account/invalid/")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
            auth.login(request, user)
        # Redirect to a success page.
            return HttpResponseRedirect("/order/")
            print 'aaaaaaa'
        else:
        # Show an error page
            return HttpResponseRedirect("/sdsdsd/sdsds/")
            print 'bbbbbb'
    else:
        return render(request,'login.html')

def index(request):
    print 'index'
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

def not_order(request):
    all_order = order_forms.objects.filter(order_status=0)
#    print all_order
    return render(request,'order/order_not.html',{'all_order':all_order})

def comm_order(request,order_id):
    comm_info = order_comment.objects.filter(order_id=order_id)
    return comm_info


def disp_order(request,id):
    order_info = order_forms.objects.get(id=id)
    comm_user = order_user.objects.get(id=order_info.faqi_user.id)
    comm_reply = order_comment.objects.filter(order_id=id)
    if request.method == "POST":
        comm_text = request.POST.get('comm_text')
        comm_or_id = id
        comm_info = order_comment(order_id=order_info,comment_text=comm_text,comment_user=comm_user)
        comm_info.save()
        return redirect('/order/disp_order/% s' % id)
    else:
        return render(request,'order/order_disp.html',{'order_info':order_info,'comm_reply':comm_reply})


def close_order(requset,id):
    close_info = order_forms.objects.get(id=id)
    close_info.order_status = 1
    close_info.save()
    return redirect('/order/not/')

def fsh_order(request):
    order_fsh_list = order_forms.objects.filter(order_status=1)
    return render(request,'order/order_fsh.html',{'order_fsh_list':order_fsh_list})

def fsh_disp(request,id):
    order_info = order_forms.objects.get(id=id)
    comm_reply = order_comment.objects.filter(order_id=id)
    return render(request,'order/fsh_disp.html',{'order_info':order_info,'comm_reply':comm_reply})


def search(request):
    if 'q' in request.GET:
        message = 'YOU SEARCHE FOR:%r' % request.GET['q']
    else:
        message = '提交为空'
    return HttpResponse(message)
