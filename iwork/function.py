# -*- coding: utf-8 -*-
from blueking.component.shortcuts import get_client_by_request
from common.log import logger
from models import Task
import base64
import celery_tasks

def get_business(request):
    """
    取出所有业务信息
    :param request:
    :return:
    """
    try:
        client = get_client_by_request(request)                     # 获取code、secret参数
        bk_token = request.COOKIES.get("bk_token")                  # 获取token参数
        client.set_bk_api_ver('v2')                                 # 以v2版本调用接口
        param = {                                                   # 以下定义search_host--查询主机接口参数
            "bk_app_code": client.app_code,
            "bk_app_secret": client.app_secret,
            "bk_token": bk_token,
        }
        res = client.cc.search_business(param)                          # 调用search_host接口
        print(res);
        return res                                        # 返回json数据
    except Exception as e:
        return_dic = {
            "result": False,
            "message": u"失败",
            "code": 0,
            "results": 0
        }
        return return_dic

def get_task(request):
    """
    取出所有任务类型信息
    :param request:
    :return:
    """
    try:
        res = Task.objects.get_task(1)                          # 调用search_host接口
        return res                                        # 返回json数据
    except Exception as e:
        return_dic = {
            "result": False,
            "message": u"失败",
            "code": 0,
            "results": 0
        }
        print("getTask Error")
        print(e)
        return return_dic


def get_host_by_bus(request):
    try:
        client = get_client_by_request(request)  # 获取code、secret参数
        bk_token = request.COOKIES.get("bk_token")  # 获取token参数
        bk_biz_id = request.GET.get("bk_biz_id")
        client.set_bk_api_ver('v2')  # 以v2版本调用接口
        param = {  # 以下定义search_host--查询主机接口参数
            "bk_app_code": client.app_code,
            "bk_app_secret": client.app_secret,
            "bk_token": bk_token,
            "condition": [
                {
                    "bk_obj_id": "biz",
                    "fields": [],
                    "condition": [
                        {
                            "field": "bk_biz_id",
                            "operator": "$eq",
                            "value": int(bk_biz_id)
                        }
                    ]
                },
            ],
            "pattern": ""
        }
        print("param")
        print(param)
        result = client.cc.search_host(param)
        print("result")
        print(result)
        return result
    except Exception as e:
        return_dic = {
            "result": False,
            "message": u"失败",
            "code": 0,
            "results": 0
        }
        return return_dic

def execute_script(request):
    try:
        client = get_client_by_request(request)  # 获取code、secret参数
        bk_token = request.COOKIES.get("bk_token")  # 获取token参数
        bk_biz_id = int(request.GET.get("bk_biz_id"))
        client.set_bk_api_ver('v2')  # 以v2版本调用接口
        encoded_ips = request.GET.get("encoded_ips")
        encoded_script = request.GET.get("encoded_script")
        ips = base64.b64decode(encoded_ips)
        print("bk_biz_id")
        print(bk_biz_id)
        ip_list= []
        for ip in ips.split(","):
            ip_list.append({
                "bk_cloud_id":0,
                "ip":ip
            })

        param = {  # 以下定义search_host--查询主机接口参数
            "bk_app_code": client.app_code,
            "bk_app_secret": client.app_secret,
            "bk_token": bk_token,
            "bk_biz_id":bk_biz_id,
            "script_param": "",
            "script_content":encoded_script,
            "script_timeout": 1000,
            "account": "root",
            "is_param_sensitive": 0,
            "script_type": 1,
            "ip_list":ip_list
        }
        result = client.job.fast_execute_script(param)
        if result.get("result"):
            job_instance_id = result.get("data").get("job_instance_id")
            ## 获取job_instance_id后启动一个轮询的celery task查询任务状态，执行完成后入库
            celery_tasks.execute_task(request,job_instance_id)
        print "execute_script param"
        print param
        print "execute_script result"
        print result
        return result
    except Exception as e:
        return_dic = {
            "result": False,
            "message": u"失败",
            "code": 0,
            "results": 0
        }
        return return_dic