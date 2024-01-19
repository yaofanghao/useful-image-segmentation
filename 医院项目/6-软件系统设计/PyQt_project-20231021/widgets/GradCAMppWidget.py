# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GradCAMppWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(999, 746)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(136, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 139, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 139, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 139, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("等线")
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(730, -10, 271, 101))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color rgb(0, 0, 0)")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton6 = QtWidgets.QPushButton(Form)
        self.pushButton6.setGeometry(QtCore.QRect(630, 690, 141, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.pushButton6.setFont(font)
        self.pushButton6.setStyleSheet("background-color: rgb(147, 149, 255);")
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton8 = QtWidgets.QPushButton(Form)
        self.pushButton8.setGeometry(QtCore.QRect(820, 690, 141, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton8.setFont(font)
        self.pushButton8.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton8.setObjectName("pushButton8")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(130, 650, 111, 20))
        self.lineEdit2.setText("")
        self.lineEdit2.setObjectName("lineEdit2")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(60, 650, 71, 20))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color rgb(0, 0, 127)")
        self.label2.setObjectName("label2")
        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(50, 119, 101, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color rgb(0, 0, 127)")
        self.label4.setObjectName("label4")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(460, 100, 281, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color rgb(0, 0, 127)")
        self.label3.setObjectName("label3")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 79, 1000, 671))
        self.listView.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.483, y1:0, x2:0.511727, y2:1, stop:0.5625 rgba(243, 222, 180, 255), stop:1 rgba(255, 255, 255, 255));")
        self.listView.setObjectName("listView")
        self.label5 = QtWidgets.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(50, 150, 400, 400))
        self.label5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label5.setText("")
        self.label5.setObjectName("label5")
        self.lineEdit5 = QtWidgets.QLineEdit(Form)
        self.lineEdit5.setGeometry(QtCore.QRect(400, 650, 131, 20))
        self.lineEdit5.setObjectName("lineEdit5")
        self.label6 = QtWidgets.QLabel(Form)
        self.label6.setGeometry(QtCore.QRect(460, 150, 400, 400))
        self.label6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label6.setText("")
        self.label6.setObjectName("label6")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(50, 580, 141, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(230, 580, 141, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.pushButton3.setObjectName("pushButton3")
        self.label7 = QtWidgets.QLabel(Form)
        self.label7.setGeometry(QtCore.QRect(310, 650, 81, 20))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(14)
        self.label7.setFont(font)
        self.label7.setStyleSheet("color rgb(0, 0, 127)")
        self.label7.setObjectName("label7")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 1091, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/tittle.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.listView.raise_()
        self.label.raise_()
        self.pushButton6.raise_()
        self.pushButton8.raise_()
        self.lineEdit2.raise_()
        self.label2.raise_()
        self.label4.raise_()
        self.label3.raise_()
        self.label5.raise_()
        self.lineEdit5.raise_()
        self.label6.raise_()
        self.pushButton2.raise_()
        self.pushButton3.raise_()
        self.label7.raise_()
        self.label2.setBuddy(self.lineEdit2)
        self.label5.setBuddy(self.lineEdit5)
        self.label6.setBuddy(self.lineEdit5)
        self.label7.setBuddy(self.lineEdit2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "热力图可视化界面"))
        self.label.setText(_translate("Form", "<html><head/><body><p>热力图可视化</p></body></html>"))
        self.pushButton6.setText(_translate("Form", "返回诊断系统\n"
"选择页面"))
        self.pushButton8.setText(_translate("Form", "退出"))
        self.label2.setText(_translate("Form", "日期"))
        self.label4.setText(_translate("Form", "图片显示"))
        self.label3.setText(_translate("Form", "<html><head/><body><p>Grad-CAM++热力图</p></body></html>"))
        self.lineEdit5.setPlaceholderText(_translate("Form", "图片所在路径"))
        self.pushButton2.setText(_translate("Form", "下一个"))
        self.pushButton3.setText(_translate("Form", "上一个"))
        self.label7.setText(_translate("Form", "图片名称"))

