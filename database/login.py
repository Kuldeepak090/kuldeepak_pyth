
from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

import sys


class MyApp(QDialog):

    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('database/welcomescreen.ui',self)
        
        

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
app.exec_()
              