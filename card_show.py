# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
import os
from cardout import Ui_Form
from PyQt5.QtMultimedia import *
import numpy_operator as npor
import cv2
import time

# 该文件的主要功能是执行显示抽卡结果的功能
# 如果有无效文件，则需要弹出窗口以及退出，防止堵塞进程
class card_show(QWidget, Ui_Form):
    # 定义两个信号 一个是重定义关闭信号 一个是播放完成的信号
    card_fin = pyqtSignal()
    closed = pyqtSignal()

    # 初始化界面
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.pushButton.clicked.connect(self.close)

        # self.pushButton.setGraphicsEffect(self.opacity_effect)
        self.card_fin.connect(self.closeit)

    # 配置界面
    def init_ui(self):
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    # 根据电脑屏幕初始化大小
    def default_size1(self):
        global w1, h1
        screen1 = QDesktopWidget().screenGeometry()
        size1 = self.geometry()
        print(size1)
        print(screen1)
        if (size1.width() < screen1.width()) & (size1.height() < screen1.height()) & \
                (size1.width() <= 1920) & (size1.height() <= 1080):
            self.setGeometry(0, 0, screen1.width(), screen1.height())
            self.label_v.setGeometry(0, 0, screen1.width()-1, screen1.height()-1)
            w1 = screen1.width() - 1
            h1 = screen1.height() - 1
        elif (size1.width() < screen1.width()) & (size1.height() < screen1.height()) & \
                (size1.width() > 1920) & (size1.height() > 1080):
            self.setGeometry(0, 0, 1920, 1080)
            self.label_v.setGeometry(0, 0, 1919, 1079)
            w1 = 1919
            h1 = 1079

        self.target_card.setGeometry(screen1.width() / 2 - 150, screen1.height() / 2 - 200, 300, 400)
        self.pushButton.setGeometry(screen1.width() / 2 - 100, screen1.height() / 2 + 200, 200, 100)

    # 外部调用 需要传入文件数组的内容
    def show_card(self, picdir):
        self.video_init()
        # self.img1 = QtGui.QPixmap(self.picdir).scaled(self.target_card.width(), self.target_card.height())
        self.picdirect = picdir

    # 定义视频图片部分
    def card_video(self):
        global video_status
        video_status = 1
        self.default_size1()
        self.playerv.play()
        self.Update2 = Update2(self.vdir)
        self.Update2.start()
        self.Update2.date2.connect(self.card_video_show)
        self.Update2.fin2.connect(self.closeit)

    # 通过label改变形成视频播放功能
    def card_video_show(self, image):
        self.label_v.setPixmap(QtGui.QPixmap(image))

    # 定义关闭的butttom
    def closeit(self):
        global video_status
        video_status = 2
        self.playerv.stop()
        self.show_grapic()
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                    "    font: 20pt \"字魂蜜桃猫体\";\n"
                                    "    color: rgba(255, 255, 255, 255);\n"
                                     " background-color: rgba(255, 255, 255, 0);" 
                                    "}")
    # 抽到的卡
    def show_grapic(self):
        self.cardpic = QtGui.QPixmap(self.picdirect).scaled(self.target_card.width(), self.target_card.height(),
                                 aspectRatioMode=Qt.KeepAspectRatio)
        print(self.cardpic)
        self.target_card.setPixmap(QtGui.QPixmap(self.cardpic))

    # 背景视频初始化
    def video_init(self):
        # 获取根目录
        self.save_video = os.getcwd() + '\\' + 'video'
        if not os.path.isdir(self.save_video):
            os.mkdir("video")

        self.count_v, self.v_files = npor.list_video(self.save_video)
        if self.v_files:
            self.vdir = npor.gachi_v_out(self.v_files, self.count_v, self.save_video)

            print(self.vdir)
            # 播放bgm初始化
            self.playerv = QMediaPlayer()
            self.mp4v_file = QMediaContent(QUrl.fromLocalFile(self.vdir))
            self.playerv.setMedia(self.mp4v_file)
            print('播放中')
            print(self.mp4v_file)
            self.card_video()
        else:
            self.no_video()
            return

    # 没视频的提示
    def no_video(self):
        self.reply1 = QMessageBox(QMessageBox.Information, "提示", "    -无背景抽卡视频-\n请检查目录下视频文件内容")
        # 添加自定义按钮
        self.reply1.addButton('知道了', QMessageBox.YesRole)
        self.reply1.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.reply1.setStyleSheet("  QPushButton {"
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
        self.reply1.buttonClicked.connect(self.close)
        font = QtGui.QFont()
        font.setFamily("字魂蜜桃猫体")
        font.setBold(True)
        font.setWeight(75)
        self.reply1.setFont(font)
        self.reply1.setIcon(0)
        self.reply1.show()

# 重定义按钮功能 主要产生结束信号 中断线程
    def keyPressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.changemouse = True

    def mouseReleaseEvent(self, e):
        global video_status
        video_status = 2
        if e.button() == Qt.LeftButton:
            self.changemouse = False
            self.card_fin.emit()
            self.playerv.stop()

    # 重写关闭功能
    def closeEvent(self, event):
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    font: 20pt \"字魂蜜桃猫体\";\n"
                                      "    color: rgba(255, 255, 255, 0);\n"
                                      "}")
        self.pushButton.setEnabled(False)
        self.target_card.setPixmap(QtGui.QPixmap(""))
        self.closed.emit()
        QWidget.closeEvent(self, event)


# 视频播放线程 使用OpenCv
class Update2(QThread):

    # 信号格式为QImage
    date2 = pyqtSignal(QtGui.QImage)
    fin2 = pyqtSignal()

    def __init__(self, dir):
        super(Update2, self).__init__()
        self.dir = dir

    # 运行线程 发射内容 信号
    def run(self):
        while True:
            cap = cv2.VideoCapture(self.dir)
            while True:
                ret = cap.grab()
                if video_status == 1:
                    if ret:
                        t0 = time.time()
                        ret, frame = cap.retrieve()
                        rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        h, w, ch = rgbImage.shape
                        bytesPerLine = ch * w
                        convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                        if w1 & h1:
                            convertToQtFormat = convertToQtFormat.scaled(w1, h1)
                        # cv2.waitKey(5)
                        self.date2.emit(convertToQtFormat)
                        t1 = time.time()
                        print("runing time is %s ms\n" % (str((t1 - t0) * 1000)))
                    else:
                        self.fin2.emit()
                        return
                elif video_status == 0:
                    continue
                else:
                    cap.release()
                    return

