# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:56:59 2018

@author: benjamin.l.solomon
"""

"""Check"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage("DnD Dicerolls")
        self.show()
 
if __name__ == '__main__':
    app = QApplication.instance()
    #Stops kernel from dying if the windows is generated multiple times
    if app is None:
        app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())