# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from getcard import Ui_getcard
from PyQt5 import QtMultimedia
from PyQt5.QtMultimediaWidgets import QVideoWidget
import time
from ffpyplayer.player import MediaPlayer

class card_func(QMainWindow, Ui_getcard):

    video_fin = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.videoinit()
        # if (size.width() < screen.width()) & (size.height() < screen.height()) & \
                #(size.width() <= 1920) & (size.height() <= 1080):
           # self.resize(screen.width(), screen.height())
        #elif (size.width() < screen.width()) & (size.height() < screen.height()) & \
         #       (size.width() > 1920) & (size.height() > 1080):
         #   self.resize(1920, 1080)
        self.musicon = self.radioButton.isChecked()
        self.Update1 = Update()
        self.Update1.start()
        self.Update1.date1.connect(self.musicplay)
        self.player.mediaStatusChanged.connect(self.alternativemusic)
        self.player1.mediaStatusChanged.connect(self.alternativemusic)
        self.video_fin.connect(self.videoinit)

    def videoinit(self):
        # 实例化图片
        self.image1 = QtGui.QImage()
        self.finishing = ''
        # 设定视频
        ff_opt = {'loop': 0}
        self.vplayer = MediaPlayer('02.mp4', ff_opts=ff_opt)
        # 时间轴
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.start()
        self.timer.timeout.connect(self.videoplay)

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        # screen = QDesktopWidget().screenGeometry()
        # size = self.geometry()
        self.pushButton.clicked.connect(self.close)
        self.pushButton_back.clicked.connect(self.showMinimized)
        self.musicinit()
        self.musicinit_re()
        self.readtime = 0

    def musicinit(self):
        self.play1 = False
        self.firstplay = True
        wavefile = QUrl.fromLocalFile('Grand.wav')
        content = QtMultimedia.QMediaContent(wavefile)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.setVolume(60)

    def musicinit_re(self):
        rewave = QUrl.fromLocalFile('Grand_01.wav')
        recontent = QtMultimedia.QMediaContent(rewave)
        self.player1 = QtMultimedia.QMediaPlayer()
        self.player1.setMedia(recontent)
        self.player1.setVolume(60)

    def musicplay(self):
        self.musicon = self.radioButton.isChecked()
        if self.firstplay:
            if self.musicon & (not self.play1):
                self.player.play()
                self.play1 = True
            elif (not self.musicon) & self.play1:
                self.player.stop()
                self.player1.stop()
                self.play1 = False
                self.firstplay = False
                print('stop0')
        elif not self.firstplay:
            if self.musicon & (not self.play1):
                self.player1.play()
                self.play1 = True
            elif (not self.musicon) & self.play1:
                self.player.stop()
                self.player1.stop()
                self.play1 = False
                print('stop1')

    def alternativemusic(self):
        self.readtime += 1
        if self.play1 & (self.readtime > 3):
            self.play1 = not self.play1
            self.firstplay = False

    def videoplay(self):
        # print('videoplay')
        frame, self.finishing = self.vplayer.get_frame()
        if frame is not None:
            img, t = frame
            self.image1 = QtGui.QImage(bytes(img.to_bytearray()[0]), img.get_size()[0], img.get_size()[1],
                               QtGui.QImage.Format_RGB888)
            self.image1 = self.image1.scaled(self.label_3.width(), self.label_3.height())
            self.label_3.setPixmap(QtGui.QPixmap.fromImage(self.image1))



class Update(QThread):
    date1 = pyqtSignal()

    def __init__(self):
        super(Update, self).__init__()

    def run(self):
        while True:
            time.sleep(0.1)
            self.date1.emit()  # 发射信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mk1 = card_func()
    mk1.show()
    sys.exit(app.exec_())

