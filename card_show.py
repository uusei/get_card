# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import os
from cardout import Ui_Form
from PyQt5 import QtMultimedia
from PyQt5.QtMultimediaWidgets import QVideoWidget
import time
from ffpyplayer.player import MediaPlayer
import sys
import numpy_operator as npor

class card_show(QWidget, Ui_Form):
    card_fin = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.pushButton.clicked.connect(self.close)

        # self.pushButton.setGraphicsEffect(self.opacity_effect)
        self.card_fin.connect(self.closeit)

    def init_ui(self):
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置不透明度
        #self.opacity_effect = QGraphicsOpacityEffect()
        #self.opacity_effect.setOpacity(0)


    def show_card(self, picdir):
        self.video_init()
        # self.img1 = QtGui.QPixmap(self.picdir).scaled(self.target_card.width(), self.target_card.height())
        self.picdirect = picdir

    def card_video(self):
        frame, self.finishing2 = self.vplayer1.get_frame()
        if frame is not None:
            img, t = frame
            self.image2 = QtGui.QImage(bytes(img.to_bytearray()[0]), img.get_size()[0], img.get_size()[1],
                               QtGui.QImage.Format_RGB888)
            self.image2 = self.image2.scaled(self.screen.width(), self.screen.height())
            self.screen.setPixmap(QtGui.QPixmap.fromImage(self.image2))
        if self.finishing2 == 'eof':
            self.closeit()

    def closeit(self):
        self.vplayer1.set_pause(True)
        self.show_grapic()
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                    "    font: 20pt \"字魂蜜桃猫体\";\n"
                                    "    color: rgba(255, 255, 255,255);\n"
                                    "}")

    def show_grapic(self):
        self.cardpic = QtGui.QPixmap(self.picdirect).scaled(self.target_card.width(), self.target_card.height(),
                                 aspectRatioMode=Qt.KeepAspectRatio)
        print(self.cardpic)
        self.target_card.setPixmap(QtGui.QPixmap(self.cardpic))

    def video_init(self):
        self.save_video = os.getcwd() + '\\' + 'video'
        if not os.path.isdir(self.save_video):
            os.mkdir("video")
        self.count_v, self.v_files = npor.list_video(self.save_video)
        self.vdir = npor.gachi_v_out(self.v_files, self.count_v, self.save_video)
        print(self.vdir)
        self.image2 = QtGui.QImage()
        self.finishing2 = ''
        self.vplayer1 = MediaPlayer(self.vdir)
        # 时间轴
        self.timer1 = QTimer()
        self.timer1.setInterval(40)
        self.timer1.start()
        self.timer1.timeout.connect(self.card_video)

    def keyPressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.changemouse = True

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.changemouse = False
            self.card_fin.emit()
            self.vplayer1.set_pause(True)

    def closeEvent(self, event):
        self.closed.emit()
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    font: 20pt \"字魂蜜桃猫体\";\n"
                                      "    color: rgba(255, 255, 255, 0);\n"
                                      "}")
        self.pushButton.setEnabled(False)
        self.target_card.setPixmap(QtGui.QPixmap(""))
        QWidget.closeEvent(self, event)
