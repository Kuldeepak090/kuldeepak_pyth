def check_prime_2():
    a= 495
    for i in range(2,a):
        if a%i ==0:
            return "non prime"
    else:
        return "prime" 

result=check_prime_2()   
print("value is",result)      
print("value",check_prime_2())      