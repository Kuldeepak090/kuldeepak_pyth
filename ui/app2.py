from PyQt5 import QtWidgets, uic
import sys

class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp,self).__init__()
        uic.loadUi('ui/untitled.ui',self)
        #interaction  
        self.PushButton.clicked.connect(self.update_ui)
        self.PushButton_2.clicked.connect(self.update_ui)

def update_ui(self):
    self.output.setText('RED')   
def update_ui(self):
    self.output.setText('green')    

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
app.exec_()