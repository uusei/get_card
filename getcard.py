# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getcard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_getcard(object):
    def setupUi(self, getcard):
        getcard.setObjectName("getcard")
        getcard.setEnabled(True)
        getcard.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(getcard.sizePolicy().hasHeightForWidth())
        getcard.setSizePolicy(sizePolicy)
        getcard.setMinimumSize(QtCore.QSize(800, 500))
        getcard.setMaximumSize(QtCore.QSize(1920, 1080))
        getcard.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/155.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        getcard.setWindowIcon(icon)
        getcard.setWindowOpacity(1.0)
        getcard.setStyleSheet("border-image: url(:/image/master1200.jpg); \n"
"border-radius: 8px;\n"
"background: transparent")
        getcard.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        getcard.setAnimated(True)
        getcard.setTabShape(QtWidgets.QTabWidget.Rounded)
        getcard.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(getcard)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setMinimumSize(QtCore.QSize(110, 30))
        self.radioButton.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("思源宋体 Heavy")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton.setStyleSheet("border-image: none;\n"
"color:#ff9292;\n"
"background-color: #ffffff;\n"
"border: 2px solid #ff9292;\n"
"border-radius: 10px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("musical-notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton.setIcon(icon1)
        self.radioButton.setIconSize(QtCore.QSize(25, 25))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(16, 16))
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/mana.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 30))
        self.label_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("字魂蜜桃猫体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border: 3px solid rgb(229, 229, 229);\n"
"border-radius: 15px;\n"
"padding: 5px 5px;\n"
"color: rgb(255, 253, 225);\n"
"border-image: none;")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_back.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_back.setStyleSheet("QPushButton {\n"
"border-image: none;\n"
"    color:#e799b0;\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e799b0;\n"
"    border-radius: 15px;\n"
"}    \n"
"QPushButton:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(231, 147, 172, 255), stop:0.795455 rgba(233, 157, 179, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: #ffffff;\n"
"    border:rgba(255, 255, 255, 0);\n"
"\n"
"}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_3.addWidget(self.pushButton_back)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("思源宋体 Heavy")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-image: none;\n"
"    color:#e799b0;\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e799b0;\n"
"    border-radius: 15px;\n"
"}    \n"
"QPushButton:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(231, 147, 172, 255), stop:0.795455 rgba(233, 157, 179, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: #ffffff;\n"
"    border:rgba(255, 255, 255, 0);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(650, 400))
        self.label_3.setMaximumSize(QtCore.QSize(1280, 720))
        self.label_3.setStyleSheet("border: 3px solid rgb(229, 229, 229);\n"
"border-radius: 8px;\n"
"border-image: none;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("思源宋体 Heavy")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"border-image: none;\n"
"    color:#aaaaff;\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #aaaaff;\n"
"    border-radius: 10px;\n"
"}    \n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/magical-scroll.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("思源宋体 Heavy")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"border-image: none;\n"
"    color:#d48bff;\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #d48bff;\n"
"    border-radius: 10px;\n"
"}    \n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/crystal-ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("思源宋体 Heavy")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"border-image: none;\n"
"    color:#ff9292;\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #ff9292;\n"
"    border-radius: 10px;\n"
"}    \n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image/star--v1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(110, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("思源宋体 Heavy")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"border-image: none;\n"
"    color:#ffaaff;\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #ffaaff;\n"
"    border-radius: 10px;\n"
"}    \n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/mana.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem7 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        getcard.setCentralWidget(self.centralwidget)

        self.retranslateUi(getcard)
        QtCore.QMetaObject.connectSlotsByName(getcard)

    def retranslateUi(self, getcard):
        _translate = QtCore.QCoreApplication.translate
        getcard.setWindowTitle(_translate("getcard", "getcard"))
        self.radioButton.setToolTip(_translate("getcard", "音乐选项"))
        self.radioButton.setText(_translate("getcard", "music"))
        self.label_2.setText(_translate("getcard", "0"))
        self.pushButton_back.setText(_translate("getcard", "-"))
        self.pushButton.setText(_translate("getcard", "×"))
        self.pushButton_4.setText(_translate("getcard", "操作说明"))
        self.pushButton_3.setText(_translate("getcard", "查看调试台"))
        self.pushButton_5.setText(_translate("getcard", "清空抽卡记录"))
        self.pushButton_2.setText(_translate("getcard", "消耗×1抽取"))
import card
