#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/16 17:20
# @Author  : 梦泽
# @File    : device_addr.py
# @Software: PyCharm
import sys
from tool import pyvisa_addr, serial_addr
from PySide6.QtWidgets import QApplication, QPushButton, QTableWidgetItem, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class DeviceAddr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('ui/mian_window.ui')
        self.ui.setWindowIcon(QIcon('ui/image/DeviceAddr.png'))
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 210)
        self.ui.tableWidget.setColumnWidth(2, 210)
        self.ui.tableWidget.setColumnWidth(3, 92)
        # self.ui.tableWidget.setColumnCount(4)
        # self.ui.tableWidget.setRowCount(60)
        # print(self.ui.tableWidget.rowCount())
        self.ui.ComButton.clicked.connect(self.filter_COM)
        self.ui.DeviceButton.clicked.connect(self.filter_device)
        self.ui.AllButton.clicked.connect(self.all_addr)
        self.all_addr()
        # self.setup_table()

    def setup_table(self, data=None):
        """
        设置表格,传入数据,显示数据，如果数据为None，清空表格
        :param data:需要显示的数据
        :return:
        """
        if data:
            for row, row_data in enumerate(data):
                # print(row, row_data)
                button = QPushButton("复制地址", self)
                button.clicked.connect(self.copy_address)
                self.ui.tableWidget.setCellWidget(row, 3, button)
                for col, (key, value) in enumerate(row_data.items()):
                    print(col, key, value)
                    value_item = QTableWidgetItem(str(value))
                    col_item = QTableWidgetItem(str(row + 1))
                    value_name_item = QTableWidgetItem(str(key))
                    self.ui.tableWidget.setItem(row, col, col_item)
                    self.ui.tableWidget.setItem(row, col + 1, value_name_item)
                    self.ui.tableWidget.setItem(row, col + 2, value_item)

    def filter_COM(self):
        """
        筛选出串口设备，传到表格函数中展示
        :return:
        """
        self.setup_table(serial_addr.get_port_desc())

    def filter_device(self):
        """
        筛选出pyvisa设备，传到表格函数中展示
        :return:
        """
        # self.setup_table(pyvisa_addr.resource_addr_desc())
        self.setup_table([
            {"D": 40},
            {"E": 50},
            {"F": 60}
        ])

    def all_addr(self):
        """
        展示所有设备，传到表格函数中展示
        :return:
        """
        # all_addr = pyvisa_addr.resource_addr_desc() + serial_addr.get_port_desc()
        # self.setup_table(all_addr)
        self.setup_table([
            {"A": 10},
            {"B": 20},
            {"C": 30}
        ])

    def copy_address(self):
        """
        复制地址到剪切板
        :return:
        """
        button = self.sender()
        # print(button)
        if button:
            row = self.ui.tableWidget.indexAt(button.pos()).row()
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
