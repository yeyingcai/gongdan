# coding:utf-8
from __future__ import unicode_literals
import datetime
from django.db import models


class order_group(models.Model):
    g_name = models.CharField(max_length=100,blank=True,null=True,verbose_name=u'组名称')

    def __str__(self):
        return self.g_name
class order_user(models.Model):
    u_name = models.CharField(max_length=100,blank=True,null=True,verbose_name=u'账号')
    u_password = models.CharField(max_length=100,blank=True,null=True,verbose_name=u'密码')
    r_name = models.CharField(max_length=100,blank=True,null=True,verbose_name=u'真是姓名')
    u_mail = models.EmailField()
    u_gid = models.ForeignKey(order_group,blank=True,null=True,verbose_name=u'组ID')

    def __str__(self):
        return self.r_name

ORDER_TYPE = (
    (1, u"监控协助"),
    (2, u"DB协助"),
    (3, u"上线协助"),
    (4, u"权限申请"),
    (5, u"主机申请"),
    (6, u"BLB申请"),
    (4, u"宽带申请"),
    (5, u"其他协助")
    )
class order_forms(models.Model):
    order_type = models.IntegerField(choices=ORDER_TYPE, blank=True, null=True, verbose_name=u"工单类型")
    order_title = models.CharField(max_length=256, blank=True, null=True, verbose_name=u"工单名称")
    order_text = models.TextField(blank=True, null=True, default='',verbose_name=u"工单内容")
    faqi_user = models.ForeignKey(order_user,blank=True,verbose_name=u'发起用户')
    order_status=models.CharField(max_length=3,default='0',verbose_name=u'工单状态')
    date_added = models.DateTimeField(auto_now=True, null=True)
    end_time = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.order_type
    class Meta:
        verbose_name = u"工单"
        verbose_name_plural = verbose_name