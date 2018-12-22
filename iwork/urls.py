# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'iwork.views',
    (r'^$', 'index'),
    (r'^get_bus$', 'get_bus'),
    (r'^get_task$', 'get_task'),
    (r'^get_host/$', 'get_host'),
    (r'^execute_script/$', 'execute_script'),
)
