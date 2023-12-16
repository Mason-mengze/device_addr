#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/16 17:09
# @Author  : 梦泽
# @File    : pyvisa_addr.py
# @Software: PyCharm

import pyvisa as visa


def resource_addr_desc() -> tuple:
    """
    获取可用资源对应的描述与对应的地址
    """
    rm = visa.ResourceManager()
    resource_list = []
    for resource in rm.list_resources():
        resource_dict = {
            rm.open_resource(resource).query('*IDN?'): resource,
        }
        resource_list.append(resource_dict)
    return tuple(resource_list)
