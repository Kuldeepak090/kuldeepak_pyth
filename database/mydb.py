
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import  datetime 


# basic setup
Base = declarative_base()

# Class for database table
class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer,primary_key = True)
    title = Column(String(100))
    rating = Column(Integer)
    added_on = Column(DateTime, default = datetime.now())

    def __str__(self): 
        return self.title 
if __name__ == "__main__":
    Base.metadata.create_all(create_engine('sqlite:///db.sqlite3')) 
