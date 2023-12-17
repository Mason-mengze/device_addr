#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/16 17:20
# @Author  : 梦泽
# @File    : device_addr.py
# @Software: PyCharm
import sys
from tool import pyvisa_addr, serial_addr
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon


class DeviceAddr:
    def __init__(self):
        self.ui = QUiLoader().load('ui/mian_window.ui')
        self.ui.setWindowIcon(QIcon('ui/image/DeviceAddr.png'))
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 210)
        self.ui.tableWidget.setColumnWidth(2, 210)
        self.ui.tableWidget.setColumnWidth(3, 92)
        # self.ui.AllButton.clicked.connect(pyvisa_addr.resource_addr_desc)
        # self.ui.ComButton.clicked.connect(serial_addr.get_port_desc)
        # self.ui.show()
        # Add a QPushButton in the third column of each row
        for row in range(self.ui.tableWidget.rowCount()):
            button = QPushButton("复制地址")
            # button.clicked.connect(self.copy_address)
            self.ui.tableWidget.setCellWidget(row, 3, button)

    # def pyvisa_addr(self):
    #     self.ui.textBrowser.setText(str(pyvisa_addr.resource_addr_desc()))
    #
    # def serial_addr(self):
    #     self.ui.textBrowser.setText(str(serial_addr.get_port_desc()))


app = QApplication(sys.argv)
stats = DeviceAddr()
stats.ui.show()
app.exec()
