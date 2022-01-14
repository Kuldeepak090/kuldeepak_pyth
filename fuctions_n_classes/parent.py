class fruit:

    def __int__(self,size,shape,flavour,color,name):
        self.size = size
        self.shape = shape
        self.color = color
        self.flavour = flavour
        self.name = name

    def show(self):
        print('name',self.name)   
        print('shape',self.shape) 
        print('flavour',self.flavour)
        print('color',self.color)
        print('size',self.size)

if __name__ == "__main__":
    a1 = fruit('apple','small')  
    a2 = fruit("orange" , "small" , "round", color = "orange")   

    a1.show() 
    a2.show()  
