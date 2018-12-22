# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class TaskManage(models.Manager):
    def get_task(self, requestData):
        """
        获取Task
        :return:    json
        """
        try:
            res = Task.objects.all().values() ##get(task_id=1)
            dict = list(res)
            print dict
            result = {"code": 0, "result": True, "data": dict, "message": u"查询成功"}
        except Exception, e:
            result = {"code": -1, "result": False, "message": u"查询失败 %s" % e}
        return result

class Task(models.Model):
    task_id = models.IntegerField(u'任务ID')
    task_name = models.CharField(u'任务名称人',max_length=64)
    task_time = models.CharField(u'任务时间',max_length=64)
    objects = TaskManage( )

