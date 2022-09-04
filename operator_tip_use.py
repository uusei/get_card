# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import card


class tip_window(QWidget):

    tip_exit = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.default_size1()
        self.dispic = QtGui.QPixmap('operator_pic.png')
        self.dispic = self.dispic.scaled(self.width(), self.height())
        self.label.setPixmap(self.dispic)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def setupUi(self, show_tip):
        show_tip.setObjectName("show_tip")
        show_tip.resize(800, 500)
        show_tip.setMinimumSize(QtCore.QSize(800, 500))
        show_tip.setMaximumSize(QtCore.QSize(1920, 1080))
        show_tip.setSizeIncrement(QtCore.QSize(0, 0))
        show_tip.setStyleSheet("")
        self.label = QtWidgets.QLabel(show_tip)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label.setMinimumSize(QtCore.QSize(800, 500))
        self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(show_tip)
        QtCore.QMetaObject.connectSlotsByName(show_tip)

    def retranslateUi(self, show_tip):
        _translate = QtCore.QCoreApplication.translate
        show_tip.setWindowTitle(_translate("show_tip", "Form"))


    def default_size1(self):
        screen1 = QDesktopWidget().screenGeometry()
        size1 = self.geometry()
        print(size1)
        print(screen1)
        if (size1.width() < screen1.width()) & (size1.height() < screen1.height()) & \
                (size1.width() <= 1920) & (size1.height() <= 1080):
            self.setGeometry(0, 0, screen1.width(), screen1.height())
            self.label.setGeometry(0, 0, screen1.width()-1, screen1.height()-1)
        elif (size1.width() < screen1.width()) & (size1.height() < screen1.height()) & \
                (size1.width() > 1920) & (size1.height() > 1080):
            self.setGeometry(0, 0, 1920, 1080)
            self.label.setGeometry(0, 0, 1919, 1079)

    def keyPressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.changemouse = True

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.changemouse = False
            self.tip_exit.emit()
            self.close()


