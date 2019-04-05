# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cyber\Desktop\paint.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
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



class MyUI(Ui_MainWindow):
    def __init__(self, MainWindow):
        super(MyUI, self).__init__()
        self.win = MainWindow
        self.setupUi(self.win)
        self.x = 0
        self.y = 0
        self.painter = QtGui.QPainter()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.draw)
        self.timer.start()


    def draw(self):
        pass
        time.sleep(1)
        try:
            print("1")
            self.painter.begin(self.centralwidget)
            print("2")
            self.painter.setPen(QColor(Qt.blue))
            self.painter.drawLine(10,100,100,100)
            print("3")
            self.painter.drawRect(self.x, self.x+100, self.y, self.y+100)
            print("({0}, {1})".format(self.x, self.y))
            self.x +=1
            self.y +=1
            self.painter.end()
            print("5")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyUI(MainWindow)

    MainWindow.show()
    app.exec_()
    #sys.exit(app.exec_())
    #MainWindow.
