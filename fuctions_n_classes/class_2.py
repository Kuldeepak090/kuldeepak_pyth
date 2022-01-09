class Preson:

    age = 12

    def greet(self):
        print("hello!")

if __name__ =="__main__":
    alex = Preson()
    alex.greet() 
    print("old age",alex.age)
    alex.age = 25
    print("new age",alex.age)       

    hari = Preson()
    hari.greet()
    print(hari.age)