from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QSplashScreen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import time

import sys


class SplashScreen(QSplashScreen):

    def __init__(self):
        super(QSplashScreen, self).__init__()
        uic.loadUi('database/welcome.ui',self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #pixmap = QPixmap("bg.jpg.jpg")
        #self.setPixmap(pixmap)

    def progress(self) :
        for i in range(100) :
            time.sleep(0.1)  
            self.progressBar.setValue(i)

class MainPage(QDialog)   :
    def __init_(self)  :
        super(QDialog,self).__init__() 
        uic.loadUi('database/Login',self)      

if __name__== '__main__':

    app = QtWidgets.QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()
    window=MainPage()
    window.show()
    
    splash.finish(window)
    
    app.exec_()