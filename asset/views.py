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

def idc_disp(request,id):
    idc_info = j_IDC.objects.get(id=id)
    return render(request,'asset/idc_disp.html',{'idc_info':idc_info})

def idc_add(request):
    if request.method == "POST":
        idc_name = request.POST.get('idc_name')
        idc_addr = request.POST.get('idc_addr')
        idc_bandwidth = request.POST.get('idc_bandwidth')
        idc_linkman = request.POST.get('idc_linkman')
        idc_phone = request.POST.get('idc_phone')
        idc_operator = request.POST.get('idc_operator')
        idc_comment = request.POST.get('idc_comment')

        idc_info = j_IDC(name=idc_name,address=idc_addr,bandwidth=idc_bandwidth,linkman=idc_linkman,phone=idc_phone,operator=idc_operator,comment=idc_comment)
        idc_info.save()
        return redirect('/asset/idc/')
    else:
        return render(request, 'asset/idc_add.html')

def host_index(request):
    host_info = j_Asset.objects.all()
    idc_info = j_IDC.objects.all()
    return render(request,'asset/host_index.html',{'host_info':host_info,'idc_info':idc_info})


def host_add(request):
    if request.method == "POST":
        host_ip = request.POST.get('host_ip')
        host_name = request.POST.get('host_name')
        host_idc = request.POST.get('host_idc')
        host_cpu = request.POST.get('host_cpu')
        host_memory = request.POST.get('host_memory')
        host_disk = request.POST.get('host_disk ')
        host_system_type = request.POST.get('host_system_type')
        host_brand = request.POST.get('host_brand')
        host_cabinet = request.POST.get('host_cabinet')
        host_position = request.POST.get('host_position')
        host_comment = request.POST.get('host_comment')
        idc_name = j_IDC.objects.get(name=host_idc)
        host_info = j_Asset(ip=host_ip,hostname=host_name,idc=idc_name,cpu=host_cpu,memory=host_memory,disk=host_disk, system_type=host_system_type,brand=host_brand,cabinet=host_cabinet,position=host_position,comment=host_comment)
        host_info.save()
        return redirect('/asset/host/')
    else:
        return render(request,'asset/host_add.html')

def vm_index(request):
    return render(request,'idc_index.html')

def net_index(request):
    return render(request,'host_index.html')

def docker_index(request):
    return render(request,'idc_index.html')

def pc_index(request):
    return render(request,'host_index.html')
