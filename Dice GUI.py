# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:56:59 2018

@author: benjamin.l.solomon
"""

"""Check"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'DnD Dicerolls'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Rolls a D20 One Time', self)
        button.setToolTip('This is an example button')
        button.resize(150,32)
        button.move(100,70)
        button.clicked.connect(self.on_click)
        
        self.statusBar().showMessage("DnD Dicerolls")
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    
if __name__ == '__main__':
    app = QApplication.instance()
    #Stops kernel from dying if the windows is generated multiple times
    if app is None:
        app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
