# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cyber\Desktop\graphicview.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.graphicsView.setObjectName("graphicsView")
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
        self.painter = QtGui.QPainter(self.graphicsView)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.draw)
        self.timer.start()


    def draw(self):

        time.sleep(1)
        try:
            painter = QtGui.QPainter(self.graphicsView)
            painter.setPen(Qt.blue)
            painter.setFont(QtGui.QFont("Arial", 30))
            painter.drawText(QRect(1,1,100,100), Qt.AlignCenter, "Qt")
            print("1")
            #self.painter.begin(self.graphicsView)
            print("2")
            self.painter.setPen(Qt.blue)
            self.painter.drawLine(10,100,100,100)
            print("3")
            self.painter.drawRect(self.x, self.x+100, self.y, self.y+100)
            print("({0}, {1})".format(self.x, self.y))
            self.x +=1
            self.y +=1
            #self.painter.end()
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
