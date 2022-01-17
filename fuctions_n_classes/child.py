from parent import fruit

class mango(fruit):
    
    def set_variety(self,v):
        self.variety = v

    def detail(self):
        self.show()
        print("variety:",self.variety) 


if __name__ =="__main__":
    m1 = mango('mango','sweet','large','oval',color ='yellow') 
    m1.set_variety('alphonso')
    m2 = mango('mango','sweet','small','oval',color ='yellow')    
    m2.set_variety('dhassheri')  


    m1.detail()   
    m2.detail() 
