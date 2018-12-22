
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from models import Task
from django.contrib import admin
@admin.register(Task)
class ConfigAdmin(admin.ModelAdmin):
    # 要展示给用户的字段
    list_display = ('task_id','task_name')
    # 让用户搜索的字段
    search_fields = ('task_id','task_name')
    # 排序的字段
    ordering = ('task_id','task_name')

    # admin.sites.register( Task )