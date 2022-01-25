from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QSplashScreen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import time
import sqlite3
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QDialog, QApplication


import sys


class Welcomescreen(QDialog):

    def __init__(self):

        super(Welcomescreen, self).__init__()
        loadUi('database/welcomescreen.ui', self)
        self.login.clicked.connect(self.gotologin)

    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi('database/Login.ui', self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields")

        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            cur = conn.cursor()
            qurey = 'SELECT password FROM login_info WHERE username =\ '' +user+ "\"'
            cur.execute(qurey)
            result_pass = cur.fetchone([0])

            if result_pass == password:
                print("Sucessfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")


class SplashScreen(QSplashScreen):

    def __init__(self):
        super(QSplashScreen, self).__init__()
        uic.loadUi('database/welcome.ui', self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #pixmap = QPixmap("bg.jpg.jpg")
        # self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class MainPage(QDialog):
    def __init_(self):
        super(QDialog, self).__init__()
        uic.loadUi('database/Login', self)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    splash = SplashScreen()
    splash.center()
    splash.show()
    splash.progress()
    window = MainPage()
    window.show()

    splash.finish(window)
    window = Welcomescreen()
    widget = QtWidgets.QStackedWidget()

    widget.addWidget(window)
    widget.setFixedHeight(500)
    widget.setFixedWidth(600)
    widget.show()
    window.show()
    app.exec_()
