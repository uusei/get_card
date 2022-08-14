# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 759)
        Form.setMinimumSize(QtCore.QSize(800, 500))
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        Form.setStyleSheet("border-radius: 8px;\n"
"")
        self.target_card = QtWidgets.QLabel(Form)
        self.target_card.setGeometry(QtCore.QRect(290, 80, 200, 300))
        self.target_card.setMinimumSize(QtCore.QSize(200, 300))
        self.target_card.setMaximumSize(QtCore.QSize(200, 300))
        self.target_card.setStyleSheet("border-radius: 8px;\n"
"border-image: none;\n"
"border-color: transparent;")
        self.target_card.setText("")
        self.target_card.setAlignment(QtCore.Qt.AlignCenter)
        self.target_card.setObjectName("target_card")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(260, 650, 200, 100))
        self.pushButton.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 100))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 20pt \"字魂蜜桃猫体\";\n"
"    color: rgba(255, 255, 255,0);    \n"
"    border-color: transparent;\n"
"}")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.screenfull = QVideoWidget(Form)
        self.screenfull.setGeometry(QtCore.QRect(9, 9, 909, 635))
        self.screenfull.setMinimumSize(QtCore.QSize(719, 400))
        self.screenfull.setMaximumSize(QtCore.QSize(1920, 1080))
        self.screenfull.setObjectName("screenfull")
        self.screenfull.raise_()
        self.target_card.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "单击此处退出"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
