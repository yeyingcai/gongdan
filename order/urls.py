#coding=utf-8
"""gongdan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from order import views as vw
from django.conf import settings
from django.conf.urls.static import static
from order import views as order_v
urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^css/(?P<path>.*)','django.views.static.serve',{'document_root':settings.CSS_ROOT}),
#    url(r'^img/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.IMG_ROOT}),
#    url(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_ROOT}),
#    url(r'^font-awesome/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.FONT_ROOT}),
#    url(r'^$', vw.index),
#    url(r'^order/$', include('order.urls')),
    url(r'^$',order_v.index),
    url(r'^add/$',order_v.add_order),
    url(r'^search/$',order_v.search),
    url(r'^not/$',order_v.not_order),
    url(r'^disp_order/(\d+)/$',order_v.disp_order),
    url(r'^close_order/(\d+)/$',order_v.close_order),
    url(r'^fsh/$',order_v.fsh_order),
    url(r'^disp_fsh/(\d+)$',order_v.fsh_disp),

]
