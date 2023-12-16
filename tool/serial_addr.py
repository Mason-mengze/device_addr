#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/16 17:08
# @Author  : 梦泽
# @File    : serial_addr.py
# @Software: PyCharm

import serial.tools.list_ports


def get_port_desc() -> tuple:
    """
    获取可用串口对应的描述与对应的地址
    """
    ports_list = []
    ports = serial.tools.list_ports.comports()
    for port in ports:
        port_dict = {
            port.description: port.device,
        }
        ports_list.append(port_dict)

    return tuple(ports_list)