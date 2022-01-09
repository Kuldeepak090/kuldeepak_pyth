def check_prime_3(n):
    for i in range(2,n):
        if n% i ==0:
            return "non prime"
        else:
            return "prime" 
def get_cube(*arg):
    for i in arg:
        yield i**3

for val in get_cube(4,5,6):
    print(val)          