# coding:utf-8
from __future__ import unicode_literals
from django.db import models
#from django.apps import AppConfig
#from django.db.models.signals import post_save
#from gongdan.asset.models import *
import datetime
# Create your models here.
ASSET_ENV = (
    (1, U'生产环境'),
    (2, U'测试环境')
    )

ASSET_STATUS = (
    (1, u"已使用"),
    (2, u"未使用"),
    (3, u"报废")
    )

ASSET_TYPE = (
    (1, u"物理机"),
    (2, u"虚拟机"),
    (3, u"Docker")
    )
PC_TYPE = (
    (1, u"台式机"),
    (2, u"笔记本")
)
ASSET_NET = (
    (1, u"防火墙"),
    (2, u"路由器"),
    (3, u"交换机"),
    (4, u"AC"),
    (5, u"AP")

)
class j_IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'机房名称')
    bandwidth = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'机房带宽')
    linkman = models.CharField(max_length=16, blank=True, null=True, default='', verbose_name=u'联系人')
    phone = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'联系电话')
    address = models.CharField(max_length=128, blank=True, null=True, default='', verbose_name=u"机房地址")
    network = models.TextField(blank=True, null=True, default='', verbose_name=u"IP地址段")
    date_added = models.DateField(auto_now=True, null=True)
    operator = models.CharField(max_length=32, blank=True, default='', null=True, verbose_name=u"运营商")
    comment = models.CharField(max_length=128, blank=True, default='', null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC机房"
        verbose_name_plural = verbose_name


class j_Asset(models.Model):
    """
    asset modle
    """
    ip = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"主机IP")
    hostname = models.CharField(unique=True, max_length=128, verbose_name=u"主机名")
    port = models.IntegerField(blank=True, null=True, verbose_name=u"端口号")
    username = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"管理用户名")
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name=u"密码")
    use_default_auth = models.BooleanField(default=True, verbose_name=u"使用默认管理账号")
    idc = models.ForeignKey(j_IDC, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'机房')
    brand = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'硬件厂商型号')
    cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
    memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
    disk = models.CharField(max_length=1024, blank=True, null=True, verbose_name=u'硬盘')
    system_type = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"系统类型")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"系统版本号")
    cabinet = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'机柜号')
    position = models.IntegerField(blank=True, null=True, verbose_name=u'机器位置')
    number = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'资产编号')
    status = models.IntegerField(choices=ASSET_STATUS, blank=True, null=True, default=1, verbose_name=u"机器状态")
    asset_type = models.IntegerField(choices=ASSET_TYPE, blank=True, null=True, verbose_name=u"主机类型")
    env = models.IntegerField(choices=ASSET_ENV, blank=True, null=True, verbose_name=u"运行环境")
    sn = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"SN编号")
    date_added = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.ip
    class Meta:
        verbose_name = u"资产"
        verbose_name_plural = verbose_name



class j_net(models.Model):
    nt_name = models.CharField(max_length=32, verbose_name=u'设备名称')
    nt_firm = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'厂商')
    nt_model = models.CharField(max_length=16, blank=True, null=True, default='', verbose_name=u'型号')
    phone = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'接口数量')
    idc = models.ForeignKey(j_IDC, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'机房')
    network = models.TextField(blank=True, null=True, default='', verbose_name=u"IP地址段")
    date_added = models.DateField(auto_now=True, null=True)
    comment = models.CharField(max_length=128, blank=True, default='', null=True, verbose_name=u"备注")
    def __unicode__(self):
        return self.nt_name

    class Meta:
        verbose_name = u"网络设备"
        verbose_name_plural = verbose_name

class j_vm(models.Model):
    ip = models.IPAddressField(max_length=32, blank=True, null=True, verbose_name=u"主机IP")
    hostname = models.CharField(unique=True, max_length=128, verbose_name=u"主机名")
    port = models.IntegerField(blank=True, null=True, verbose_name=u"端口号")
    username = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"管理用户名")
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name=u"密码")
    use_default_auth = models.BooleanField(default=True, verbose_name=u"使用默认管理账号")
    cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
    memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
    disk = models.CharField(max_length=1024, blank=True, null=True, verbose_name=u'硬盘')
    system_type = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"系统类型")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"系统版本号")
    date_added = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    idc = models.ForeignKey(j_Asset, blank=True, null=True,  on_delete=models.SET_NULL, verbose_name=u'宿主机')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name = u"虚拟机"
        verbose_name_plural = verbose_name

class j_docker(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"主机名")
    ssh_ip = models.TextField(blank=True, null=True, default='',verbose_name=u"ssh地址")
    ssh_port = models.CharField(max_length=12,null=True, blank=True, verbose_name=u"ssh端口")
    service = models.CharField(max_length=64, blank=True, null=True, verbose_name=u"服务")
    port = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"服务端口")
    p_host = models.ForeignKey(j_Asset, blank=True, null=True,verbose_name=u"宿主机")
    img_name = models.CharField(max_length=24, blank=True, null=True, verbose_name=u"镜像名称")
    file_path = models.TextField(blank=True, null=True, verbose_name=u"DOCKERFILE")
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")
    def __unicode__(self):
        return self.ssh_ip

    class Meta:
       verbose_name = u"docker"
       verbose_name_plural = verbose_name
class j_pc(models.Model):
   brand = models.CharField(max_length=32,blank=True,null=True, verbose_name=u"品牌")
   pc_type = models.IntegerField(choices=PC_TYPE, blank=True, null=True, verbose_name=u"类型")
   cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u"CPU")
   mem = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"内存")
   disk = models.CharField(max_length=12, blank=True, null=True, verbose_name=u"硬盘")
   sn = models.CharField(max_length=64, blank=True, null=True, verbose_name=u"资产编码")
   owner = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"使用人")
   comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")

   def __unicode__(self):
       return self.owner

   class Meta:
       verbose_name = u"PC主机"
       verbose_name_plural = verbose_name