class Dog:

    # special method to setup the perameteres of the class (constructor)

    def __init__(self,brd,age,gdr,voice):
         # dynamic attributes of the dog class
        self.breed = brd
        self.age = age
        self.gender = gdr
        self.voice = voice

    def bark(self) :
        print("dog is barking")
        print(self.voice * 3)  

    def show(self):
        print(self.breed)  
        print(self.age)
        print(self.gender)
        print(self.voice)   

if __name__ == "__main__":
    moti = Dog("doberman",5,'M',"bow")
    tommy = Dog("german shephard",10,"F","bew")
    print(tommy)
    tommy.show()
    print(moti)
    moti.show()
    tommy.bark()
    moti.bark()
