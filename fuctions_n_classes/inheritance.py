class ListX(list):

    def sum_value(self):
        return sum(self)

    def mean_value(self):
        return sum(self)/len(self)   

    def max_value(self):
        return max(self)    

x = ListX()  
for i in range(10):
    x.append(int(input(">> value >>>")))  


print(x.sum_value()) 
print(x.mean_value())
print(x.mean_value())     