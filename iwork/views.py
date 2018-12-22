# -*- coding: utf-8 -*-

from common.mymako import render_json
from common.mymako import render_mako_context
import function


def index(request):
    """
    首页
    """

    return render_mako_context(request, '/iwork/index.html')


def get_bus(request):
    result = function.get_business(request)
    return render_json(result)

def get_task(request):
    result = function.get_task(request)
    return render_json(result)

def get_host(request):
    result = function.get_host_by_bus(request)
    return render_json(result)

def execute_script(request):
    result = function.execute_script(request)
    return render_json(result)