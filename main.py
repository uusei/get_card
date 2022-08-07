# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from getcard import Ui_getcard
from PyQt5 import QtMultimedia
from PyQt5.QtMultimediaWidgets import QVideoWidget
import time


class card_func(QMainWindow, Ui_getcard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        # if (size.width() < screen.width()) & (size.height() < screen.height()) & \
                #(size.width() <= 1920) & (size.height() <= 1080):
           # self.resize(screen.width(), screen.height())
        #elif (size.width() < screen.width()) & (size.height() < screen.height()) & \
         #       (size.width() > 1920) & (size.height() > 1080):
         #   self.resize(1920, 1080)
        self.musicon = self.radioButton.isChecked()
        self.Update1 = Update(self.musicon, self.play1)
        self.Update1.start()
        self.Update1.date1.connect(self.musicplay)
        self.Update1.stop1.connect(self.musicstop)

    def init_ui(self):
        self.play1 = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        # screen = QDesktopWidget().screenGeometry()
        # size = self.geometry()
        self.pushButton.clicked.connect(self.close)
        self.pushButton_back.clicked.connect(self.showMinimized)
        self.musicinit()


    def musicinit(self):
        wavefile = QUrl.fromLocalFile('Grand.wav')
        content = QtMultimedia.QMediaContent(wavefile)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.setVolume(60)

    def musicplay(self):
        self.player.play()
        self.play1 = True

    def musicstop(self):
        self.player.stop()
        self.play1 = False


class Update(QThread):
    date1 = pyqtSignal()
    stop1 = pyqtSignal()

    def __init__(self, musicon, play1):
        super(Update, self).__init__()
        self.musicon = musicon
        self.play1 = play1

    def run(self):
        while self.musicon:
            if not self.play1:
                self.sleep(1)
                self.date1.emit()  # 发射信号
                # print(1)
            elif self.play1:
                self.sleep(1)
                self.stop1.emit()  # 发射信号




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mk1 = card_func()
    mk1.show()
    sys.exit(app.exec_())

