def get_cubes_old(*arg):
    x =[]
    for i in arg:
        x.append(i**3)
    return x
print(get_cubes_old(1,2,3,4,5,))    



def get_cube(*arg):
    for i in arg:
        yield i**3

for val in get_cube(23,44):
    print(val)