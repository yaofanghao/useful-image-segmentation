# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InitWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(967, 629)
        widget.setFocusPolicy(QtCore.Qt.ClickFocus)
        widget.setStyleSheet("")
        self.pushButton1 = QtWidgets.QPushButton(widget)
        self.pushButton1.setGeometry(QtCore.QRect(570, 280, 181, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(140, 200, 200);")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(widget)
        self.pushButton2.setGeometry(QtCore.QRect(570, 370, 181, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(140, 200, 200);")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(widget)
        self.pushButton3.setGeometry(QtCore.QRect(780, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton3.setObjectName("pushButton3")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(0, -80, 1001, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/background.png"))
        self.label.setObjectName("label")
        self.label1_2 = QtWidgets.QLabel(widget)
        self.label1_2.setGeometry(QtCore.QRect(220, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label1_2.setFont(font)
        self.label1_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 10, 40);")
        self.label1_2.setObjectName("label1_2")
        self.label.raise_()
        self.pushButton3.raise_()
        self.pushButton2.raise_()
        self.pushButton1.raise_()
        self.label1_2.raise_()
        self.label1_2.setBuddy(self.pushButton1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "基于人工智能的ME-NBI辅助诊断软件系统"))
        self.pushButton1.setText(_translate("widget", "辅助诊断肠化亚型"))
        self.pushButton2.setText(_translate("widget", "OLGIM综合评估"))
        self.pushButton3.setText(_translate("widget", "退出"))
        self.label1_2.setText(_translate("widget", "AI辅助ME-NBI诊断病变软件系统"))
import widgets.apprcc
