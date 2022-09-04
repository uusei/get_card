# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
import numpy as np
from PyQt5.QtGui import QCursor
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class record_window(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.pushButton.clicked.connect(self.close)

    def setupUi(self, show_record):
        show_record.setObjectName("show_record")
        show_record.resize(400, 400)
        show_record.setMinimumSize(QtCore.QSize(400, 400))
        show_record.setStyleSheet("background-color: #ffffff;\n"
                                  "    border: 2px solid #ff9292;\n"
                                  "    border-radius: 6px;")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(show_record)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(show_record)
        self.label.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily("字魂蜜桃猫体")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                 "border: none;\n"
                                 "color: #ff9292;\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(show_record)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color: #ff9292;\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "color: #ffffff;\n"
                                      "border-color: #ff9292;\n"
                                      "background-color: #ff9292;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(show_record)
        self.textEdit.setMinimumSize(QtCore.QSize(380, 350))
        self.textEdit.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: #ff9292;\n"
                                    "border: 2px solid #ff9292;\n"
                                    "border-radius: 5px;")
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(show_record)
        QtCore.QMetaObject.connectSlotsByName(show_record)

    def retranslateUi(self, show_record):
        _translate = QtCore.QCoreApplication.translate
        show_record.setWindowTitle(_translate("show_record", "record"))
        self.label.setText(_translate("show_record", "记录以及信息"))
        self.pushButton.setText(_translate("show_record", "×"))

    def print_record(self):
        self.textEdit.setText('正在读取抽卡记录\n')
        if os.path.isfile('receive_card.npy'):
            self.textEdit.append('您的抽卡记录如下（按时间由近到远）：\n')
            receive = np.load('receive_card.npy')
            record_num = len(receive)
            for i in range(record_num):
                self.textEdit.append(str(receive[i]))
        else:
            self.textEdit.append('暂无本地抽卡记录\n')
        self.textEdit.append('\n')
        self.textEdit.append('提示：如果在运行后更换卡池请点击-更新玛娜-刷新\n')
        self.textEdit.append('提示：若无法正常播放视频请安装依赖文件夹下的LAV_filters\n')
        self.textEdit.append('提示：若无法正常显示字体请到文件夹下安装字体\n')
        self.textEdit.append('提示：为排除本地无文件问题，请到目录下寻找以下文件:\n')
        self.textEdit.append('02.mp4 Grand.wav Grand_1.wav\n')
        self.textEdit.append('文件夹pic,video是否为空\n')
        self.textEdit.append('其中pic对应卡面 video对应背景视频\n')
        self.textEdit.append('提示：发生闪退、崩溃、卡顿请联系QQ2362003458\n')

    def mousePressEvent(self, e):
        self.__dragWin = True
        self.__dragWin_x = e.x()
        self.__dragWin_y = e.y()
        self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, e):
        # 移动gif题
        if self.__dragWin == True:
            pos = e.globalPos()
            self.move(pos.x() - self.__dragWin_x, pos.y() - self.__dragWin_y)

    def mouseReleaseEvent(self, e):
        self.__dragWin = False
        self.setCursor(QCursor(Qt.ArrowCursor))
