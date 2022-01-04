def check_prime_3(n):
    for i in range(2,n):
        if n% i ==0:
            return "non prime"
        else:
            return "prime" 

print("15 is", check_prime_3(15))               

x =[12,34,567,9]
for i in x:
    print(f'{i} is {check_prime_3(i)}')


num = int(input("enter the number:"))
print(f" {num} :{check_prime_3(num)}")   