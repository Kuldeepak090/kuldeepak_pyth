###add 5 to each element of given list [12,45,67,7,21]

def c():
    c_list = [12,45,67,7,21]
    for num in range(0,len(c_list)):
        c_list[num]+=5
    return c_list
print(c())