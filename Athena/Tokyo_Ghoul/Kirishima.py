#encoding=utf-8
from Athena.Tokyo_Ghoul.Kaneziki import Ui_Kaneziki
import PyQt4, sys
from PyQt4.QtGui import QMainWindow
import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4 import QtGui
from Athena.Akame_ga_KILL.Tatsumi import Tatsumi
from Athena.Akame_ga_KILL.Mine import Mine


class Kirishima(QMainWindow, Ui_Kaneziki):


    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("work()"))

    #开始进行任务抓取
    @QtCore.pyqtSlot()
    def work(self):
        urls = []
        urls.append(str(self.lineEdit.text()))
        mine = Mine()
        dm = Tatsumi(mine)
        dm.import_urls(urls)
        dm.start()


app = PyQt4.QtGui.QApplication(sys.argv)
kirishima = Kirishima()
kirishima.show()
sys.exit(app.exec_())