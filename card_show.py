# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import os
from cardout import Ui_Form
from PyQt5.QtMultimedia import *
from ffpyplayer.player import MediaPlayer
import numpy_operator as npor
import time

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
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置不透明度
        #self.opacity_effect = QGraphicsOpacityEffect()
        #self.opacity_effect.setOpacity(0)

    def default_size1(self):
        screen1 = QDesktopWidget().screenGeometry()
        size1 = self.geometry()
        print(size1)
        print(screen1)
        if (size1.width() < screen1.width()) & (size1.height() < screen1.height()) & \
                (size1.width() <= 1920) & (size1.height() <= 1080):
            self.setGeometry(0, 0, screen1.width(), screen1.height())
            self.screenfull.setGeometry(0, 0, screen1.width()-2, screen1.height()-2)
        elif (size1.width() < screen1.width()) & (size1.height() < screen1.height()) & \
                (size1.width() > 1920) & (size1.height() > 1080):
            self.setGeometry(0, 0, 1920, 1080)
            self.screenfull.setGeometry(0, 0, 1920, 1080)

        self.target_card.setGeometry(screen1.width(), screen1.height() / 2 - 200, 200, 300)
        self.pushButton.setGeometry(screen1.width(), screen1.height() / 2 + 200, 200, 100)

    def show_card(self, picdir):
        self.video_init()
        # self.img1 = QtGui.QPixmap(self.picdir).scaled(self.target_card.width(), self.target_card.height())
        self.picdirect = picdir

    def card_video(self):
        self.default_size1()
        self.playerv.play()
        self.Update2 = Update2()
        self.Update2.start()
        self.Update2.date2.connect(self.is_state)

    def is_state(self):
        self.vstate = self.playerv.MediaStatus()
        print(self.vstate)
        if self.vstate == '7':
            self.closeit()

    def closeit(self):
        self.playerv.stop()
        self.show_grapic()
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                    "    font: 20pt \"字魂蜜桃猫体\";\n"
                                    "    color: rgba(255, 255, 255, 255);\n"
                                    "}")
        screen1 = QDesktopWidget().screenGeometry()
        self.target_card.setGeometry(screen1.width() / 2 - 100, screen1.height() / 2 - 200, 200, 300)
        self.pushButton.setGeometry(screen1.width() / 2 - 100, screen1.height() / 2 + 200, 200, 100)
        self.Update2.quit()
    # 抽到的卡
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
        self.playerv = QMediaPlayer()
        self.mp4v_file = QMediaContent(QUrl.fromLocalFile(self.vdir))
        self.playerv.setVideoOutput(self.screenfull)
        self.playerv.setMedia(self.mp4v_file)
        print('播放中')
        print(self.mp4v_file)
        # print(self.mp4_file)
        self.card_video()

    def keyPressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.changemouse = True

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.changemouse = False
            self.card_fin.emit()
            self.playerv.stop()

    def closeEvent(self, event):
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    font: 20pt \"字魂蜜桃猫体\";\n"
                                      "    color: rgba(255, 255, 255, 0);\n"
                                      "}")
        self.pushButton.setEnabled(False)
        self.target_card.setPixmap(QtGui.QPixmap(""))
        self.closed.emit()
        QWidget.closeEvent(self, event)

class Update2(QThread):
    date2 = pyqtSignal()

    def __init__(self):
        super(Update2, self).__init__()

    def run(self):
        while True:
            time.sleep(1)
            self.date2.emit()  # 发射信号