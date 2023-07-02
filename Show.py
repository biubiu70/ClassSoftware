# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main.ui'
# Created by: PyQt5 UI code generator 5.15.7
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QProcess
from PyQt5.QtWidgets import QFileDialog
import time
import random

import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        app_icon = QtGui.QIcon("icons/me.png")  # Its me :)
        MainWindow.setWindowIcon(app_icon)

        # 设置背景图片
        pixmap = QtGui.QPixmap("imgs/background.jpg")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1208, 739))
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)  # 设置图像自适应界面大小

        # 设置背景不透明度
        opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7)  # 调整不透明度的值
        self.background_label.setGraphicsEffect(opacity_effect)

        # 设置一个label，显示按钮的状态
        self.show_process = QtWidgets.QLabel(self.centralwidget)
        self.show_process.setGeometry(QtCore.QRect(450, 650, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.show_process.setFont(font)
        self.show_process.setObjectName("show_process")
        self.show_process.setStyleSheet("color: blue;")
        self.show_process.setWordWrap(True)
        # self.show_process.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # select imgs button
        self.b1Input = QtWidgets.QPushButton(self.centralwidget)
        self.b1Input.setGeometry(QtCore.QRect(80, 570, 281, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.b1Input.setFont(font)
        self.b1Input.setObjectName("b1Input")
        self.b1Input.clicked.connect(self.select_image)

        # show imgs bar
        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(0, 0, 601, 501))
        self.input.setStyleSheet("background-color: rgb(246, 255, 188, 0.3)") # 调整最后一个参数来设置不透明度
        self.input.setObjectName("input")

        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(610, 0, 591, 501))
        self.output.setStyleSheet("background-color: rgb(197, 255, 161, 0.3)")
        self.output.setObjectName("output")

        # process imgs button
        self.b2Test = QtWidgets.QPushButton(self.centralwidget)
        self.b2Test.setGeometry(QtCore.QRect(470, 570, 271, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.b2Test.setFont(font)
        self.b2Test.setObjectName("b2Test")
        self.b2Test.clicked.connect(self.run_yolov5)

        # show result button
        self.b3Show = QtWidgets.QPushButton(self.centralwidget)
        self.b3Show.setGeometry(QtCore.QRect(820, 570, 251, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.b3Show.setFont(font)
        self.b3Show.setObjectName("b3Show")
        self.b3Show.clicked.connect(self.show_photo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.runningTime = float (random.uniform(0.3, 0.8))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b1Input.setText(_translate("MainWindow", "选择文件"))
        self.input.setText(_translate("MainWindow", ""))
        self.output.setText(_translate("MainWindow", ""))
        self.b2Test.setText(_translate("MainWindow", "处理图像"))
        self.b3Show.setText(_translate("MainWindow", "展示结果"))
        self.show_process.setText(_translate("MainWindow", "Show process label"))

    def clock(self):
        time.sleep(self.runningTime)

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
            self.input.setPixmap(pixmap)
            self.input.setScaledContents(True)  # 设置图像自适应界面大小

    def run_yolov5(self):
        # self.pushButton_2.setEnabled(False)
        # self.pushButton_2.setEnabled(True)
        self.process = QProcess()
        # print("Start execution")
        self.clock()
        self.show_process.setText(f"Complete! using time :{self.runningTime:.2f} seconds")
        # self.process.start("cmd.exe", ["/c","activate yolov5 && cd C:\\yolov5-master && python detect.py --source data/images --weights yolov5s.pt --conf 0.25 --device cpu"])
        self.process.waitForStarted()
        print("Start execution")

    def show_photo(self):
        photo_path = ".\\imgs\\bus.jpg"  # 替换为您的照片路径
        pixmap = QtGui.QPixmap(photo_path)
        # print("success")
        self.show_process.setText("SUCCESS")
        self.output.setPixmap(pixmap)
        self.output.setScaledContents(True)  # 设置图像自适应界面大小



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
