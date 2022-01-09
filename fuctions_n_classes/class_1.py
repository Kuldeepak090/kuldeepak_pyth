class MyNewClass :
    '''this is  a boring that i've created'''
    pass

class Preson:
    '''this is a simple person class'''
    # attribute of class
    age = 12

    #method of class
    def greet(self):
        print("hello!")

if __name__== "__main__":
    print(Preson.age)
    print(Preson.greet)
    print(Preson.__doc__)


# to use class we should create object of the class    