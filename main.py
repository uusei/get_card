# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from getcard import Ui_getcard
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
import time
import numpy_operator as npor
import numpy as np
import card_show
from showrecord import record_window
from PyQt5.QtGui import QCursor
import cv2
import operator_tip_use


class card_func(QMainWindow, Ui_getcard):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.musicon = self.radioButton.isChecked()
        self.Update1 = Update()
        self.Update1.start()
        self.Update_s = Update1()
        self.Update_s.start()
        self.Update1.date1.connect(self.musicplay)
        self.videoinit()
        self.player.mediaStatusChanged.connect(self.alternativemusic)
        self.player1.mediaStatusChanged.connect(self.alternativemusic)
        self.pushButton_2.clicked.connect(self.gachicard)
        self.pushButton_4.clicked.connect(self.tipit)
        self.pushButton_5.clicked.connect(self.update_card)
        self.Update_s.date2.connect(self.video_size)
        self.pushButton_3.clicked.connect(self.recordit)

    # 设置默认大小
    def default_size(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        # 关于大小支持 目前仅支持到1920*1080为止 由于本人硬件有限 高分辨率暂时不做支持
        # 为防止2K、4K高分辨率出现问题 请不要随意拖拽界面
        if (size.width() < screen.width()) & (size.height() < screen.height()) & \
                (size.width() <= 1920) & (size.height() <= 1080):
            self.setGeometry(0, 0, screen.width(), screen.height())
        elif (size.width() < screen.width()) & (size.height() < screen.height()) & \
                (size.width() > 1920) & (size.height() > 1080):
            self.setGeometry(0, 0, 1920, 1080)

    # 初始化开始界面
    def videoinit(self):
        global video_status, w1, h1
        video_status = 1
        w1 = 719
        h1 = 400
        self.Update_v = Update_v()
        self.Update_v.start()
        self.Update_v.video2label.connect(self.videoplay)

    # 实时变换视频大小
    def video_size(self):
        self.screenfull_w = self.screenfull.geometry().width()
        self.screenfull_h = self.screenfull.geometry().height()
        global w1, h1
        w1 = self.screenfull_w
        h1 = self.screenfull_h

    # 配置界面
    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        # screen = QDesktopWidget().screenGeometry()
        # size = self.geometry()
        self.default_size()
        self.pushButton.clicked.connect(self.close)
        self.pushButton_back.clicked.connect(self.showMinimized)
        self.musicinit()
        self.musicinit_re()
        self.readtime = 0
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.update_card()

    # 初始化BGM
    def musicinit(self):
        self.play1 = False
        self.firstplay = True
        wavefile = QUrl.fromLocalFile('Grand.wav')
        content = QMediaContent(wavefile)
        self.player = QMediaPlayer()
        self.player.setMedia(content)
        self.player.setVolume(60)

    # 初始化第二段BGM 用于衔接初始BGM 后续仍然重播此段BGM
    def musicinit_re(self):
        rewave = QUrl.fromLocalFile('Grand_01.wav')
        recontent = QMediaContent(rewave)
        self.player1 = QMediaPlayer()
        self.player1.setMedia(recontent)
        self.player1.setVolume(60)

    # 读取并按照逻辑播放BGM，如上所示
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

    # 当音频状态发生反转，记录的值也发生反转
    def alternativemusic(self):
        self.readtime += 1
        if self.play1 & (self.readtime > 3):
            self.play1 = not self.play1
            self.firstplay = False

    # 将帧图片显示在label上
    def videoplay(self, image):
        self.screenfull.setPixmap(QtGui.QPixmap(image))

    # messagebox 提示玛娜不足
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

    # 执行抽卡功能
    def gachicard(self):
        if self.label_2.text() == '0':
            self.lack_mana()
        # 进行抽选
        else:
            # self.player2.stop()
            global video_status
            video_status = 0
            self.radioButton.setChecked(False)
            # 得到抽到的目录 得到图片数组位置
            self.picdir, self.initpic = npor.gachi_card_out(self.pic, self.count_pic)
            # 将图片输出到新窗口
            self.Dialogue.show()
            self.Dialogue.show_card(self.picdir)

    # 保存目前的玛娜数值到本地npy
    def save_num(self):
        self.pic = np.delete(self.pic, self.initpic)
        self.count_pic -= 1
        self.label_2.setText(str(self.count_pic))

        np.save('picnum1', self.pic)
        print(self.pic)
        self.radioButton.setChecked(True)
        global video_status
        video_status = 1
        self.Update_v.start()
        # self.player2.play()

    # 更新玛娜按钮
    def update_card(self):
        self.Dialogue = card_show.card_show()
        # 得到图片数组 得到数组长度
        self.pic, self.count_pic = npor.read_num()
        self.label_2.setText(str(self.count_pic))
        self.Dialogue.closed.connect(self.save_num)

    # 调试台以及抽卡记录
    def recordit(self):
        self.record_Widget = record_window()
        self.record_Widget.show()
        self.record_Widget.print_record()

    def tipit(self):
        self.tip_widget = operator_tip_use.tip_window()
        self.tip_widget.show()

#   以下都是重写功能 主要实现两大功能

#   拖拽功能
    def mousePressEvent(self, e):
        global video_status
        video_status = 2
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
        global video_status
        video_status = 1
        self.__dragWin = False
        self.setCursor(QCursor(Qt.ArrowCursor))

#  多线程 功能 播放02.mp4 修改请改为同名
class Update(QThread):
    date1 = pyqtSignal()

    def __init__(self):
        super(Update, self).__init__()

    def run(self):
        while True:
            time.sleep(0.1)
            self.date1.emit()  # 发射信号


# 线程1 实现音频的开关问题
class Update1(QThread):
    date2 = pyqtSignal()

    def __init__(self):
        super(Update1, self).__init__()

    def run(self):
        while True:
            time.sleep(0.1)
            self.date2.emit()  # 发射信号

# 线程1 实现视频播放功能
class Update_v(QThread):
    video2label = pyqtSignal(QtGui.QImage)

    def __init__(self):
        super(Update_v, self).__init__()

    def run(self):
        cap = cv2.VideoCapture('02.mp4')
        while True:
            ret = cap.grab()
            if video_status == 1:
                if ret:
                    ret, frame = cap.retrieve()
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgbImage.shape
                    bytesPerLine = ch * w
                    convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                    if w1 & h1:
                        convertToQtFormat = convertToQtFormat.scaled(w1, h1)
                    cv2.waitKey(20)
                    self.video2label.emit(convertToQtFormat)
                else:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue
            elif video_status == 2:
                continue
            else:
                cap.release()
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mk1 = card_func()
    mk1.show()
    sys.exit(app.exec_())

