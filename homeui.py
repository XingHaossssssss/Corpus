# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeui(object):
    def setupUi(self, homeui):
        homeui.setObjectName("homeui")
        homeui.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(homeui)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 140, 341, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 140, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(230, 200, 441, 301))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(670, 200, 20, 301))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        homeui.setCentralWidget(self.centralwidget)

        self.retranslateUi(homeui)
        QtCore.QMetaObject.connectSlotsByName(homeui)

    def retranslateUi(self, homeui):
        _translate = QtCore.QCoreApplication.translate
        homeui.setWindowTitle(_translate("homeui", "Corpus"))
        self.pushButton.setText(_translate("homeui", "查询"))
