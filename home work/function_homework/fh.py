def check_prime():
    a = 541
    for i in range(2,a):
        if a%i==0:
            a = i**3
            print("not a prime")
            break
    else:
         print("prime") 
if __name__ == "__main__" :
    check_prime() 