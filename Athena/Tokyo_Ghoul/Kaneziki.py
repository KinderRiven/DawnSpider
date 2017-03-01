# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kaneziki.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Kaneziki(object):
    def setupUi(self, Kaneziki):
        Kaneziki.setObjectName(_fromUtf8("Kaneziki"))
        Kaneziki.resize(602, 62)
        self.centralwidget = QtGui.QWidget(Kaneziki)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 461, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 20, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Kaneziki.setCentralWidget(self.centralwidget)

        self.retranslateUi(Kaneziki)
        QtCore.QMetaObject.connectSlotsByName(Kaneziki)

    def retranslateUi(self, Kaneziki):
        Kaneziki.setWindowTitle(_translate("Kaneziki", "dm1080p", None))
        self.pushButton.setText(_translate("Kaneziki", "提取", None))

