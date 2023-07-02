"""
继承HG的代码，需要在这个基础上修改
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QProcess


class CommandExecutor(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.process = QProcess()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 20, 72, 15))
        self.label.setObjectName("label")

        # 文件选择按键
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 93, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.select_image) # 链接按钮触发函数

        # 初始化图片显示框
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 111, 101))
        self.label_3.setStyleSheet("background-color: rgb(225, 255, 246);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 72, 15))
        self.label_4.setObjectName("label_4")

        # 开始检测按键
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 310, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.run_yolov5) # 链接按钮触发函数

        # 显示检测按键
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 390, 111, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.show_photo)

        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(260, 470, 72, 15))
        self.label_2.setObjectName("label_2")
        # 检测图片显示框
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(60, 60, 451, 361))
        self.label_5.setStyleSheet("background-color: rgb(225, 255, 246);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "功能选择"))
        self.pushButton.setText(_translate("MainWindow", "文件查找"))
        self.label_4.setText(_translate("MainWindow", "初始图片"))
        self.pushButton_2.setText(_translate("MainWindow", "开始检测"))
        self.pushButton_3.setText(_translate("MainWindow", "显示检测"))
        self.label_2.setText(_translate("MainWindow", "检测显示"))

    def select_image(self):
        # 打开文件对话框以选择一个图片文件
        file_dialog = QFileDialog(MainWindow)
        # 图片格式为bmp、png和jpg
        file_dialog.setNameFilter("Image files (*.bmp *.png *.jpg)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            # 加载选择的图片文件
            image_file_path = file_dialog.selectedFiles()[0]
            pixmap = QtGui.QPixmap(image_file_path)
            self.label_3.setPixmap(pixmap)
            self.label_3.setScaledContents(True)  # 设置图像自适应界面大小

    def run_yolov5(self):
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setEnabled(True)

        self.process = QProcess()
        print("1")
        self.process.start("cmd.exe", ["/c","activate yolov5 && cd C:\\yolov5-master && python detect.py --source data/images --weights yolov5s.pt --conf 0.25 --device cpu"])
        self.process.waitForStarted()
        print("3")

    def show_photo(self):
        print("4")
        photo_path = "C:\\yolov5-master\\runs\\detect\\exp3\\bus.jpg"  # 替换为您的照片路径
        pixmap = QtGui.QPixmap(photo_path)
        print("5")
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)  # 设置图像自适应界面大小

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
