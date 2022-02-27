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
        loadUi('welcomescreen.ui', self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotosingup)
        
        

    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosingup(self) :
        signup = CreateAccScreen()  
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocontinue(self) :
        continue_2 = FillProfileScreen()  
        widget.addWidget(continue_2)
        widget.setCurrentIndex(widget.currentIndex()+1)    



class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi('Login.ui', self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields")

        else:
            conn = sqlite3.connect("shop.sqlite")
            cur = conn.cursor()
            cur = conn.cursor()
            qurey = f'''SELECT password FROM login_info WHERE username = '{user}' '''
            print(qurey) 
            cur.execute(qurey)
            result_pass = cur.fetchone()
            print(result_pass)

            if result_pass[0] == password:
                print("Sucessfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen,self).__init__() 
        loadUi('createacc.ui', self) 
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)    
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)   
        self.signup.clicked.connect(self.signupfunction) 

    def signupfunction(self):
        user = self.emailfield.text()  
        password = self.passwordfield.text()  
        confirmpassword = self.confirmpasswordfield.text()   

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please fill in all input") 

        elif password!=confirmpassword:
            self.error.setText("Password do not match")

        else:
           conn = sqlite3.connect("shop.sqlite")
           cur = conn.cursor() 

           user_info = [user, password]
           cur.execute('INSERT INTO login_info (username,password) VALUES (?,?)', user_info)

           conn.commit()
           conn.close()

           fillprofile = FillProfileScreen()
           widget.addWidget(fillprofile)
           widget.setCurrentIndex(widget.currentIndex()+ 1)
        

class FillProfileScreen(QDialog) :
    def __init__(self):
        super(FillProfileScreen,self).__init__()

        loadUi('fill form.ui',self)
       # self.image.setPixmap(QPixmap('placeholder.png'))
         
        self.continue_2.clicked.connect(self.continuefunction) 

    def continuefunction(self):
        username = self.uname.text()  
        firstname = self.fname.text()  
        lastname = self.lname.text()
        date=self.dateEdit.date()
        male = self.male.isChecked()
        female= self.female.isChecked()
        print(username,firstname,lastname,date,male,female)

        conn = sqlite3.connect("shop.sqlite")
        cur = conn.cursor() 

        user_info = [firstname,lastname,username,str(date),0 if male else 1]

        cur.execute("insert into info (fname, lname,uname,dob, gender) values (?,?,?,?,?)",user_info)

        conn.commit()
        conn.close()
          

class SplashScreen(QSplashScreen):

    def __init__(self):
        super(QSplashScreen, self).__init__()
        uic.loadUi('welcome.ui', self)
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
        uic.loadUi('Login', self)


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

