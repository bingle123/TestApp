# -*- coding: utf-8 -*-

import time
from celery import task
from blueking.component.shortcuts import get_client_by_request

@task()
def async_task(job_instance_id):
    print "here1"
    # client = get_client_by_request(request)  # 获取code、secret参数
    # bk_token = request.COOKIES.get("bk_token")  # 获取token参数
    # bk_biz_id = int(request.GET.get("bk_biz_id"))
    # client.set_bk_api_ver('v2')  # 以v2版本调用接口
    # print "here2"
    # params = {
    #     "bk_app_code": client.app_code,
    #     "bk_app_secret": client.app_secret,
    #     "bk_token": bk_token,
    #     "bk_biz_id":bk_biz_id,
    #     "job_instance_id":job_instance_id
    # }
    # while not client.job.get_job_instance_status(params).get('data').get('is_finished'):
    #     print 'waiting job finished...'
    #     time.sleep(2)
    # result = client.job.get_job_instance_log(params)
    # print "here3"
    # print(result)


def execute_task(request,job_instance_id):
    print "here"
    try:
        async_task.delay(job_instance_id)
    except Exception as e:
        print "heredddd"
        print e
