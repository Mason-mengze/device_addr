#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/16 17:09
# @Author  : 梦泽
# @File    : pyvisa_addr.py
# @Software: PyCharm

import pyvisa as visa


def resource_addr_desc() -> list:
    """
    获取可用资源对应的描述与对应的地址
    """
    rm = visa.ResourceManager()
    resource_list = []
    for resource in rm.list_resources():
        try:
            res = rm.open_resource(resource)
            resource_dict = {
                res.query('*IDN?'): resource,
            }
        except visa.VisaIOError:
            # 处理未能识别的仪器
            resource_dict = {
                '未知设备': resource,
            }
        resource_list.append(resource_dict)
    return resource_list


if __name__ == '__main__':
    print(resource_addr_desc())
