from PyQt5 import QtWidgets, uic
import sys



class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp,self).__init__()
        uic.loadUi('ui/caculator.ui',self)
        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connected(self.method_2)
        self.push_3.clicked.connected(self.method_3)
        self.push_4.clicked.connected(self.method_4)
        self.push_5.clicked.connected(self.method_5)
        self.push_6.clicked.connected(self.method_6)
        self.push_7.clicked.connected(self.method_7)
        self.push_8.clicked.connected(self.method_8)
        self.push_9.clicked.connected(self.method_9)
        self.push_0.clicked.connected(self.method_0)
        self.push_add.clicked.connected(self.method_add)
        self.push_sub.clicked.connected(self.method_sub)
        self.push_multi.clicked.connected(self.method_multi)
        self.push_div.clicked.connected(self.method_div)
        self.push_dot.clicked.connected(self.method_dot)
        self.push_del.clicked.connected(self.method_del)
        self.push_clear.clicked.connected(self.method_clear)
        self.push_equal.clicked.connected(self.method_equal)

def method_1(self):
    text = self.label.text()
    self.label.setText(text+"1")  

def method_2(self):
    text = self.label.text()
    self.label.setText(text+"2")  

def method_3(self):
    text = self.label.text()
    self.label.setText(text+"3") 

def method_4(self):
    text = self.label.text()
    self.label.setText(text+"4")  

def method_5(self):
    text = self.label.text()
    self.label.setText(text+"5")  

def method_6(self):
    text = self.label.text()
    self.label.setText(text+"6")  

def method_7(self):
    text = self.label.text()
    self.label.setText(text+"7")   

def method_8(self):
    text = self.label.text()
    self.label.setText(text+"8")  

def method_9(self):
    text = self.label.text()
    self.label.setText(text+"9")  

def method_0(self):
    text = self.label.text()
    self.label.setText(text+"0")   

def method_add(self):
    text = self.label.text()
    self.label.setText(text+"+")  

def method_sub(self):
    text = self.label.text()
    self.label.setText(text+"-")  

def method_multi(self):
    text = self.label.text()
    self.label.setText(text+"*")  

def method_div(self):
    text = self.label.text()
    self.label.setText(text+"/")  

def method_dot(self):
    text = self.label.text()
    self.label.setText(text+".")

def method_del(self):
    text = self.label.text()
    self.label.setText(text[:len(text)-1])  

def method_clear(self):
    self.label.setText("")  

def method_1(self):
    text = self.label.text()
    self.label.setText(text+"1")  

def method_equal(self):
    text = self.label.text()
    
    try:    
        ans=eval(text)
        self.label.setText(str(ans)) 
    except:
        self.lable.setText("Wrong Input")                   

        #done

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
app.exec_()