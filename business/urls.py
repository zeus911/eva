#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from business import views
from business import platfapi
from business.dnsmanage import views as dnsviews

urlpatterns = [
##业务
    url(r'^business_add/$', views.business_add, name="business_add"),
    url(r'^business_list/$', views.business_list, name="business_list"),
    url(r'^business_delete/(?P<uuid>[^/]+)/$', views.business_delete, name="business_delete"),
    url(r'^business_edit/(?P<uuid>[^/]+)/$', views.business_edit, name="business_edit"),
    url(r'^business_detail/(?P<uuid>[^/]+)/$', views.business_detail, name="business_detail"),
##查看配置文件
    url(r'^business/conf/show',views.business_conf_show,name="business_conf_show"),
    url(r'^business/conf/create',views.deploy_nginx_tmp_file,name="deploy_nginx_tmp_file"),


##BUG
    url(r'^bugs_list/$', views.bugs_list, name="bugs_list"),

##平台
    url(r'^platform_list/$', views.platform_list, name="platform_list"),
    url(r'^platform_detail/(?P<uuid>[^/]+)/$', views.platform_detail, name="platform_detail"),
    url(r'^platform_edit/(?P<uuid>[^/]+)/$', views.platform_edit, name="platform_edit"),
    url(r'^platform_add/$', views.platform_add, name="platform_add"),
    # url(r'^platform_delete/$', views.platform_delete, name="platform_delete"),


##IP管理
    url(r'^domain_ip_list/$', views.domain_ip_list, name="domain_ip_list"),
    url(r'^domain_ip_add/$', views.domain_ip_add, name="domain_ip_add"),
    url(r'^domain_ip_edit/(?P<uuid>[^/]+)/$', views.domain_ip_edit, name="domain_ip_edit"),
    url(r'^domain_ip_delete/(?P<uuid>[^/]+)/$', views.domain_ip_delete, name="domain_ip_delete"),



##域名
    url(r'^domain_list/$', views.domain_list, name="domain_list"),
    url(r'^domain_add/$', views.domain_add, name="domain_add"),
    url(r'^domain_edit/(?P<uuid>[^/]+)/$', views.domain_edit, name="domain_edit"),
    url(r'^domain_delete/(?P<uuid>[^/]+)/$', views.domain_delete, name="domain_delete"),
    url(r'^domain_detail/(?P<uuid>[^/]+)/$', views.domain_detail, name="domain_detail"),
    url(r'^domain_add_batch/$', views.domain_add_batch, name="domain_add_batch"),


##更新域名至服务器
    url(r'^domain_rsync/(?P<uuid>[^/]+)/$', views.business_domain_rsync, name="domain_rsync"),
    url(r'^domain_rsync_to_server/$', views.domain_rsync_to_server, name="domain_rsync_to_server"),



##域名监控
    url(r'^domain/monitor/(?P<uuid>[^/]+)/$',views.domain_monitor,name="domain_monitor"),
    url(r'^domain/change_monitor_status/',views.change_domain_monitor_status,name="change_domain_monitor_status"),
    url(r'^domain/get_status/',views.get_domain_status,name="get_domain_status"),
    url(r'^domain/get_code/',views.get_domain_code,name="get_domain_code"),
    url(r'^domain/monitor_restart/',views.restart_all_monitor,name="restart_all_monitor"),


##白名单
##API
    url(r'^platform_api/$', platfapi.get_platform_data),

##域名管理
    url(r'^domain/manage/user/list/$', dnsviews.dnsuser_list, name="dnsuser_list"),
    url(r'^domain/manage/user/add/$',dnsviews.dnsuser_add,name="dnsuser_add"),
    url(r'^domain/manage/user/delete/(?P<id>[^/]+)/$',dnsviews.dnsuser_delete,name="dnsuser_delete"),
    url(r'^domain/manage/user/edit/(?P<id>[^/]+)/$',dnsviews.dnsuser_edit,name="dnsuser_edit"),
    url(r'^domain/manage/user/domain/pull/(?P<id>[^/]+)/$',dnsviews.dnsuser_get_domainname,name="dnsuser_get_domainname"),


    url(r'^domain/manage/domain/list/1$', dnsviews.dnsname_list, name="dnsname_list"),
    url(r'^domain/manage/domain/add/$', dnsviews.dnsname_add_one, name="dnsname_add_one"),
    url(r'^domain/manage/domain/remark/$', dnsviews.dnsname_domain_remark, name="dnsname_domain_remark"), #更新域名备注

    url(r'^domain/manage/domain/status/$', dnsviews.dnsname_status_change, name="dnsname_status_change"),

    url(r'^domain/manage/domain/delete/(?P<id>[^/]+)/$', dnsviews.dnsname_delete, name="dnsname_delete"),
    url(r'^domain/manage/domain/detail/(?P<id>[^/]+)/$', dnsviews.dnsname_detail, name="dnsname_detail"),
    url(r'^domain/manage/domain/records/(?P<id>[^/]+)/$', dnsviews.dnsname_get_records, name="dnsname_get_records"),

##记录管理
    url(r'^domain/manage/records/add/(?P<id>[^/]+)/$',dnsviews.dnsname_add_records,name="dnsname_add_records"),
    url(r'^domain/manage/record/add/(?P<id>[^/]+)/$',dnsviews.dnsname_add_one_record,name="dnsname_add_one_record"),
    url(r'^domain/manage/record/modify/(?P<uuid>[^/]+)/$',dnsviews.dnsname_record_modify,name="dnsname_record_modify"),
    url(r'^domain/manage/record/delete/(?P<uuid>[^/]+)/$',dnsviews.dnsname_record_delete,name="dnsname_record_delete"),
    url(r'^domain/manage/record/standby/$', dnsviews.dnsname_record_standby, name="dnsname_record_standby"),
    url(r'^domain/manage/record/switcher/$', dnsviews.dnsname_record_switcher, name="dnsname_record_switcher"),
    url(r'^domain/manage/record/list/$', dnsviews.dnsname_record_list, name="dnsname_record_list"),
    url(r'^domain/manage/record/status/$', dnsviews.dnsname_record_status, name="dnsname_record_status"), #改变记录状态


##一键转移域名
    url(r'^domain/manage/domain/transfer/(?P<uuid>[^/]+)/$', dnsviews.dnsname_transfer, name="dnsname_transfer"),





]