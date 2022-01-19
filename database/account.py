from turtle import title
from PyQt5 import QtWidgets, uic
from git import sys
from matplotlib import widgets
from matplotlib.widgets import Widget

class Welcomescreen(QtWidgets.QMainWindow):

    def __init__(self):
        super(Welcomescreen, self).__init__()
        uic.loadUi('database/welcomescreen.ui',self)
        self.login.clicked.connect(self.gotologin)

    def gotologin(self):
        login = Login() 
        Widget.addWidget(login)
        Widget.setCurrentIndex(Widget.currentIndex()+1)


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('database/Login.ui',self)          

app = QtWidgets.QApplication(sys.argv)
window = Welcomescreen()
window.show()
app.exec_()        