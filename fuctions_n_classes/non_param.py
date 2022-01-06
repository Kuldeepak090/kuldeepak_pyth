# function should not print and take input inside its code block
def check_prime():
    a = 541
    for i in range(2,a):
        if a%i==0:
            print("not a prime")
            break
    else:
         print("prime")   
if __name__ == "__main__" :
    check_prime()                      
