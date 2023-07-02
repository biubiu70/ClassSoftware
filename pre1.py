# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main.ui'
# bad UI, just for test
# Created by: PyQt5 UI code generator 5.15.7
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QProcess
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        MainWindow.setCentralWidget(self.centralwidget)

        app_icon = QtGui.QIcon("icons/me.png")  # Its me :)
        MainWindow.setWindowIcon(app_icon)  

        # Create vertical layout for central widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create horizontal layout for buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # select imgs button
        self.b1Input = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.b1Input.setFont(font)
        self.b1Input.setObjectName("b1Input")
        self.b1Input.clicked.connect(self.select_image)
        self.horizontalLayout.addWidget(self.b1Input)

        # process imgs button
        self.b2Test = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.b2Test.setFont(font)
        self.b2Test.setObjectName("b2Test")
        self.b2Test.clicked.connect(self.run_yolov5)
        self.horizontalLayout.addWidget(self.b2Test)

        # show result button
        self.b3Show = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.b3Show.setFont(font)
        self.b3Show.setObjectName("b3Show")
        self.b3Show.clicked.connect(self.show_photo)
        self.horizontalLayout.addWidget(self.b3Show)

        # Add horizontal layout to vertical layout
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Create label for input image
        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setStyleSheet("background-color: rgb(246, 255, 188)")
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)

        # Create label for output image
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setStyleSheet("background-color: rgb(197, 255, 161)")
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)

        # Set central widget for MainWindow
        MainWindow.setCentralWidget(self.centralwidget)

        # Set up other MainWindow properties
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 26))
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
        self.b1Input.setText(_translate("MainWindow", "选择文件"))
        self.b2Test.setText(_translate("MainWindow", "处理图像"))
        self.b3Show.setText(_translate("MainWindow", "展示结果"))

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
        print("Start execution")
        # self.process.start("cmd.exe", ["/c","activate yolov5 && cd C:\\yolov5-master && python detect.py --source data/images --weights yolov5s.pt --conf 0.25 --device cpu"])
        self.process.waitForStarted()

    def show_photo(self):
        photo_path = "E:\\StudyProgram\\ClassSoftware\\imgs\\bus.jpg"  # 替换为您的照片路径
        pixmap = QtGui.QPixmap(photo_path)
        print("success")
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
