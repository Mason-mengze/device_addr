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
    # print(f'资源数量:{len(rm.list_resources())}')
    for index, resource in enumerate(rm.list_resources()):
        # print(f'resource:{resource}')
        try:
            res = rm.open_resource(resource)
            res.timeout = 500   # 设置超时时间
            resource_dict = {
                res.query('*IDN?'): resource,
            }
        except visa.VisaIOError:
            # 处理未能识别的仪器
            # print(f'资源{resource}不可用')
            resource_dict = {
                'None' + str(index+1): resource,
            }
        resource_list.append(resource_dict)
    return resource_list


if __name__ == '__main__':
    print(resource_addr_desc())
