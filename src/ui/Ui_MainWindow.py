# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Oct  1 20:01:48 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(360, 300)
        MainWindow.setMinimumSize(QtCore.QSize(360, 201))
        MainWindow.setMaximumSize(QtCore.QSize(360, 300))
        MainWindow.setWindowTitle(_fromUtf8("ResizeIMG"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/1/cool.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 25, 331, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.archivo = QtGui.QRadioButton(self.centralwidget)
        self.archivo.setGeometry(QtCore.QRect(10, 90, 121, 17))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/1/paintq.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archivo.setIcon(icon1)
        self.archivo.setChecked(True)
        self.archivo.setObjectName(_fromUtf8("archivo"))
        self.directorio = QtGui.QRadioButton(self.centralwidget)
        self.directorio.setGeometry(QtCore.QRect(10, 110, 121, 17))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/1/My Pictures3.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.directorio.setIcon(icon2)
        self.directorio.setObjectName(_fromUtf8("directorio"))
        self.directorior = QtGui.QRadioButton(self.centralwidget)
        self.directorior.setGeometry(QtCore.QRect(10, 130, 271, 17))
        self.directorior.setIcon(icon2)
        self.directorior.setObjectName(_fromUtf8("directorior"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 150, 121, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/1/OK.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 100, 16, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 120, 16, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.xval = QtGui.QLineEdit(self.centralwidget)
        self.xval.setGeometry(QtCore.QRect(300, 100, 50, 20))
        self.xval.setObjectName(_fromUtf8("xval"))
        self.yval = QtGui.QLineEdit(self.centralwidget)
        self.yval.setGeometry(QtCore.QRect(300, 120, 50, 20))
        self.yval.setObjectName(_fromUtf8("yval"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 45, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 60, 331, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.log = QtGui.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(10, 190, 341, 91))
        self.log.setAcceptDrops(False)
        self.log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log.setReadOnly(True)
        self.log.setObjectName(_fromUtf8("log"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(0, 150, 231, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Entrada:", None, QtGui.QApplication.UnicodeUTF8))
        self.archivo.setText(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.directorio.setText(QtGui.QApplication.translate("MainWindow", "Directorio", None, QtGui.QApplication.UnicodeUTF8))
        self.directorior.setText(QtGui.QApplication.translate("MainWindow", "Directorio y todos sus subdirectorios", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Redimensionar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.xval.setText(QtGui.QApplication.translate("MainWindow", "1024", None, QtGui.QApplication.UnicodeUTF8))
        self.yval.setText(QtGui.QApplication.translate("MainWindow", "768", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Salida:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Log:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Remplazar archivo(s) original(es)", None, QtGui.QApplication.UnicodeUTF8))

import RS
