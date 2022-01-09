#### Create a list of 25 numbers and then generate a list with each element a cube of original value.

def f():
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    nums2 = list(map(lambda i: i ** 3, nums))
    return nums2
print(f())