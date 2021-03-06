# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:56:59 2018

@author: benjamin.l.solomon
"""

"""Check"""
import Diceroll
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
        
        button1D20 = QPushButton('Rolls a D20 One Time', self)
        button1D20.setToolTip('This is a 1D20 roll')
        button1D20.resize(150,32)
        button1D20.move(100,70)
        button1D20.clicked.connect(self.on_click)
        
        button2D8 = QPushButton('Rolls a D8 Two Times', self)
        button2D8.setToolTip('This is a 2D8 roll')
        button2D8.resize(150,32)
        button2D8.move(400,70)
        button2D8.clicked.connect(self.on_click)
        
        self.statusBar().showMessage("DnD Dicerolls")
        self.show()
 
    def button_handler():
        Roll1D20 = Diceroll.n_sided(20,1)
        
    
    @pyqtSlot()
    def on_click(self):
        #print('PyQt5 button click')
        print(Diceroll.n_sided(20,1))

    
if __name__ == '__main__':
    app = QApplication.instance()
    #Stops kernel from dying if the windows is generated multiple times
    if app is None:
        app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
