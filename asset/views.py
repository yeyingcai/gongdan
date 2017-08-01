#coding=utf-8
from django.shortcuts import *
from django.http import HttpResponse
from order.models import *
from asset.models import *
import sys
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')
@login_required(login_url='/login/')
def idc_index(request):
    idc_info = j_IDC.objects.all()
    return render(request,'asset/idc_index.html',{'idc_info':idc_info})
@login_required(login_url='/login/')
def idc_disp(request,id):
    idc_info = j_IDC.objects.get(id=id)
    return render(request,'asset/idc_disp.html',{'idc_info':idc_info})
@login_required(login_url='/login/')
def idc_del(request,id):
    del_info = j_IDC.objects.get(id=id).delete()
    idc_info = j_IDC.objects.all()
    return render(request,'asset/idc_index.html',{'idc_info':idc_info})
@login_required(login_url='/login/')
def idc_up(request,id):
    if request.method == "POST":
        idc_info = j_IDC.objects.get(id=id)
        idc_name = request.POST.get('idc_name')
        idc_info.name = idc_name
        idc_addr = request.POST.get('idc_addr')
        idc_info.address=idc_addr
        idc_bandwidth = request.POST.get('idc_bandwidth')
        idc_info.bandwidth = idc_bandwidth
        idc_linkman = request.POST.get('idc_linkman')
        idc_info.linkman = idc_linkman
        idc_phone = request.POST.get('idc_phone')
        idc_info.phone = idc_phone
        idc_operator = request.POST.get('idc_operator')
        idc_info.operator = idc_operator
        idc_comment = request.POST.get('idc_comment')
        idc_info.comment = idc_comment
        idc_info.save()
        idc_info = j_IDC.objects.all()
        return render(request, 'asset/idc_index.html', {'idc_info': idc_info})
    else:
        idc_info = j_IDC.objects.get(id=id)
        return render(request,'asset/idc_update.html',{'idc_info':idc_info})

@login_required(login_url='/login/')
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
@login_required(login_url='/login/')
def host_index(request):
    host_info = j_Asset.objects.all()
    idc_info = j_IDC.objects.all()
    return render(request,'asset/host_index.html',{'host_info':host_info,'idc_info':idc_info})
@login_required(login_url='/login/')
def host_del(request,id):
    del_info = j_Asset.objects.get(id=id).delete()
    host_info = j_Asset.objects.all()
    idc_info = j_IDC.objects.all()
    return render(request,'asset/host_index.html',{'host_info':host_info,'idc_info':idc_info})
@login_required(login_url='/login/')
def host_up(request,id):
    if request.method == "POST":
        host_info = j_Asset.objects.get(id=id)
        host_ip = request.POST.get('host_ip')
        host_info.ip = host_ip
        host_name = request.POST.get('host_name')
        host_info.hostname = host_name
        host_idc = request.POST.get('host_idc')
#        host_info.idc = host_idc
        host_cpu = request.POST.get('host_cpu')
        host_info.cpu = host_cpu
        host_memory = request.POST.get('host_memory')
        host_info.memory = host_memory
        host_disk = request.POST.get('host_disk')
        host_info.disk = host_disk
        host_system_type = request.POST.get('host_system_type')
        host_info.system_type = host_system_type
        host_brand = request.POST.get('host_brand')
        host_info.brand = host_brand
        host_cabinet = request.POST.get('host_cabinet')
        host_info.cabinet = host_cabinet
        host_position = request.POST.get('host_position')
        host_info.position = host_position
        host_comment = request.POST.get('host_comment')
        host_info.comment = host_comment
        idc_name = j_IDC.objects.get(name=host_idc)
        host_info.idc = idc_name
        host_info.save()
        return redirect('/asset/host/')
    else:
        host_info = j_Asset.objects.get(id=id)
        idc_info = j_IDC.objects.all()
        return render(request,'asset/host_up.html',{'host_info':host_info,'idc_info':idc_info})

@login_required(login_url='/login/')
def host_add(request):
    if request.method == "POST":
        host_ip = request.POST.get('host_ip')
        host_name = request.POST.get('host_name')
        host_idc = request.POST.get('host_idc')
        host_cpu = request.POST.get('host_cpu')
        host_memory = request.POST.get('host_memory')
        host_disk = request.POST.get('host_disk')
        host_system_type = request.POST.get('host_system_type')
        host_brand = request.POST.get('host_brand')
        host_cabinet = request.POST.get('host_cabinet')
        host_position = request.POST.get('host_position')
        host_comment = request.POST.get('host_comment')
        idc_name = j_IDC.objects.get(name=host_idc)
        print host_disk
        host_info = j_Asset(ip=host_ip,hostname=host_name,idc=idc_name,cpu=host_cpu,memory=host_memory,disk=host_disk, system_type=host_system_type,brand=host_brand,cabinet=host_cabinet,position=host_position,comment=host_comment)
        host_info.save()
        return redirect('/asset/host/')
    else:
        idc_info = j_IDC.objects.all()
        return render(request,'asset/host_add.html',{'idc_info':idc_info})
@login_required(login_url='/login/')
def vm_index(request):
    return render(request,'idc_index.html')
@login_required(login_url='/login/')
def net_index(request):
    return render(request,'host_index.html')
@login_required(login_url='/login/')
def docker_index(request):
    return render(request,'idc_index.html')
@login_required(login_url='/login/')
def pc_index(request):
    return render(request,'host_index.html')
