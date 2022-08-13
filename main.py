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
import numpy_operator as npor
import numpy as np
import card_show

class card_func(QMainWindow, Ui_getcard):

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
        self.pushButton_2.clicked.connect(self.gachicard)
        self.pushButton_5.clicked.connect(self.update_card)


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
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.update_card()

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

    def lack_mana(self):
        self.reply = QMessageBox(QMessageBox.Information, "提示", "\t    -玛娜不足-\n请重置抽卡次数或者更换卡池文件内容")
        # 添加自定义按钮
        self.reply.addButton('知道了', QMessageBox.YesRole)
        self.reply.addButton('也不是不可以啦', QMessageBox.NoRole)
        self.reply.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

        self.reply.setStyleSheet("  QPushButton {"
                                 "  padding: 5px 5px;"
                                 "  color:#ffffff;"
                                 "  border: 2px solid #ff9292;"
                                 "  border-radius: 2px;"
                                 "  background-color: #ff9292"
                                 "  }"
                                 "QLabel{"
                                 "  font-size: 18px;"
                                 "  padding: 5px 5px;"
                                 "  color:#ff9292;"
                                 "  }"
                                 )
        font = QtGui.QFont()
        font.setFamily("字魂蜜桃猫体")
        font.setBold(True)
        font.setWeight(75)
        self.reply.setFont(font)
        # icon = QMessageBox.
        # icon.addPixmap(QtGui.QPixmap(":/image/155.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reply.setIcon(0)
        # 设置消息框中内容前面的图标
        # self.reply.setIcon(1)
        self.reply.show()

        print('玛娜不足，请重置抽卡次数或者更换卡池文件内容')

    def gachicard(self):
        if self.label_2.text() == '0':
            self.lack_mana()
        # 进行抽选
        else:
            self.timer.stop()
            self.vplayer.set_pause(True)
            self.radioButton.setChecked(False)
            # 得到抽到的目录 得到图片数组位置
            self.picdir, self.initpic = npor.gachi_card_out(self.pic, self.count_pic)
            # 将图片输出到新窗口
            self.Dialogue.show()
            self.Dialogue.show_card(self.picdir)


    def save_num(self):
        self.pic = np.delete(self.pic, self.initpic)
        self.count_pic -= 1
        self.label_2.setText(str(self.count_pic))
        np.save('picnum1', self.pic)
        print(self.pic)
        self.timer.start()
        self.radioButton.setChecked(True)
        self.vplayer.set_pause(False)

    def update_card(self):
        self.Dialogue = card_show.card_show()
        # 得到图片数组 得到数组长度
        self.pic, self.count_pic = npor.read_num()
        self.label_2.setText(str(self.count_pic))
        self.Dialogue.closed.connect(self.save_num)

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

