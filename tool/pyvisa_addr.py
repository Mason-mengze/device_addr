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
    for index, resource in enumerate(rm.list_resources()):
        print(f'resource:{resource}')
        try:
            resource_dict = {
                rm.open_resource(resource).query('*IDN?'): resource,
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
