#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/16 17:20
# @Author  : 梦泽
# @File    : device_addr.py
# @Software: PyCharm
import sys
import pyvisa_py
from tool import pyvisa_addr, serial_addr
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class DeviceAddr(QMainWindow):
    def __init__(self):
        """
        初始化,加载ui文件,设置窗口图标,设置窗口大小,设置表格样式,设置表格列宽,设置按钮点击事件,启动时设置默认展示全部设备
        """
        super().__init__()
        self.ui = QUiLoader().load('ui/mian_window.ui')  # 加载ui文件
        self.ui.setWindowIcon(QIcon('ui/image/DeviceAddr.png'))  # 设置窗口图标
        self.ui.setFixedSize(self.ui.width(), self.ui.height())  # 设置窗口大小,不可以全屏化
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")  # 设置表头样式
        # 设置表格每列列宽
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 210)
        self.ui.tableWidget.setColumnWidth(2, 210)
        self.ui.tableWidget.setColumnWidth(3, 92)
        # 设置按钮点击事件
        self.ui.ComButton.clicked.connect(self.filter_COM)
        self.ui.DeviceButton.clicked.connect(self.filter_device)
        self.ui.AllButton.clicked.connect(self.all_addr)
        # 启动时设置默认展示全部设备
        self.all_addr()

    def setup_table(self, data=None):
        """
        设置表格,传入数据,显示数据，如果数据为None，清空表格
        :param data:需要显示的数据
        :return:
        """
        self.ui.tableWidget.clearContents()  # 清空表格,不包括表头
        if data:
            for row, row_data in enumerate(data):
                # print(row, row_data)
                # 定义复制按钮
                button = QPushButton("复制地址", self)
                button.clicked.connect(self.copy_address)
                self.ui.tableWidget.setCellWidget(row, 3, button)
                for col, (key, value) in enumerate(row_data.items()):
                    # print(col, key, value)
                    # 定义单元格内容
                    value_item = QTableWidgetItem(str(value))
                    col_item = QTableWidgetItem(str(row + 1))
                    value_name_item = QTableWidgetItem(str(key))
                    # 需要展示的内容第几行第几列单元格展示
                    self.ui.tableWidget.setItem(row, col, col_item)
                    self.ui.tableWidget.setItem(row, col + 1, value_name_item)
                    self.ui.tableWidget.setItem(row, col + 2, value_item)

    def filter_COM(self):
        """
        筛选出串口设备，传到表格函数中展示
        :return:
        """
        # 展示串口设备
        self.setup_table(serial_addr.get_port_desc())

    def filter_device(self):
        """
        筛选出pyvisa设备，传到表格函数中展示
        :return:
        """
        # 展示pyvisa设备
        self.setup_table(pyvisa_addr.resource_addr_desc())
        # self.setup_table([
        #     {"D": 40},
        #     {"E": 50},
        #     {"F": 60},
        #     {"G": 70}
        # ])

    def all_addr(self):
        """
        展示所有设备，传到表格函数中展示
        :return:
        """
        # 展示串口设别与pyvisa全部设备
        all_addr = pyvisa_addr.resource_addr_desc() + serial_addr.get_port_desc()
        self.setup_table(all_addr)
        # self.setup_table([
        #     {"A": 10},
        #     {"B": 20},
        #     {"C": 30}
        # ])

    def copy_address(self):
        """
        复制地址到剪切板
        :return:
        """
        button = self.sender()
        # print(button)
        if button:
            # 如果点击则获取点击按钮所在行的地址
            row = self.ui.tableWidget.indexAt(button.pos()).row()
            # 复制所选的单元格内容到剪切板
            address = self.ui.tableWidget.item(row, 2).text()
            # print(address)
            QApplication.clipboard().setText(address)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    stats = DeviceAddr()
    stats.ui.show()
    app.exec()
