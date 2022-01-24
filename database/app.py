
from PyQt5 import QtWidgets, uic
import sys
from mydb import Books, create_engine
from sqlalchemy.orm import sessionmaker

class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('database/books.ui',self)
        self.btnsave.clicked.connect(self.add_new_book)
        self.display_books()

    # database connection code
    def opendb(self):
        engine = create_engine('sqlite:///db.sqlite3')
        Session = sessionmaker(bind=engine)
        return Session()

    def add_new_book(self):
        title = self.editTitle.text() 
        rating = self.editRating.text() 
        if len(title) >= 3:
            db = self.opendb()
            b= Books(title=title,rating=int(rating))
            db.add(b)
            db.commit()
            db.close()
            self.statusBar().showMessage("Book Saved to Db")
            self.editTitle.setText("")
            self.editRating.setValue(5)
            self.display_books()
        else:
            self.statusBar().showMessage("Booktitle must be minimum 3 characters")    

    
    def display_books(self):
        db = self.opendb()
        books = db.query(Books).all()
        bklist = ""
        for item in books:
            bklist += f'{item.id}. {item.title} {item.rating}\n' 
        self.bkList.setText(bklist) 
        db.close()           
       
app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
app.exec_()