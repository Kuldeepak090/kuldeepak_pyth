

import sqlite3
from PyQt5 import QtWidgets 

from PyQt5.QtWidgets import QDialog, QApplication

from PyQt5.uic import loadUi
import sys

class Welcomescreen(QDialog):

    def __init__(self):
        
        super(Welcomescreen, self).__init__()
        loadUi('database/welcomescreen.ui',self)
        self.login.clicked.connect(self.gotologin)

    def gotologin(self):
        login = Login() 
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Login(QDialog):
    
    def __init__(self):
        super(Login, self).__init__()
        loadUi('database/Login.ui',self) 
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)  
        self.login.clicked.connect(self.loginfunction)   

    def loginfunction(self):
        user = self.emailfield.text()  
        password = self.passwordfield.text()  

        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields")   

        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            cur= conn.cursor()  
            qurey = 'SELECT password FROM login_info WHERE username =\ '' +user+ "\"'
            cur.execute(qurey)
            result_pass = cur.fetchone([0])

            if result_pass == password:
                print("Sucessfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")    


app = QtWidgets.QApplication(sys.argv)
window = Welcomescreen()
widget = QtWidgets.QStackedWidget()

widget.addWidget(window)
widget.setFixedHeight(500)
widget.setFixedWidth(600)   
widget.show()
window.show()
app.exec_()


