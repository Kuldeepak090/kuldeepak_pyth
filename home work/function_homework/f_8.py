### remove all the duplicate values from the given list [1,2,2,2,1,1,2,2,2,1,2,2,2,2,2,2,1,1,2,3]

def d():
    list = [1,2,2,2,1,1,2,2,2,1,2,2,2,2,2,2,1,1,2,3]
    for num in list:
        if list.count(num) > 1:
            for i in range(0,list.count(num)):
                list.pop(num)
    return list
print(d())