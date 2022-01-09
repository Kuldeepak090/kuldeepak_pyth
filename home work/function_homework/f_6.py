
### create a list from 1 to 100 and then display the sum of all the even in it.

def b():
    b_list = []
    total = 0
    for i in range(101):
        b_list.append(i)
        if i%2 == 0:
            total+=i
    return total
print(b())