### WAP to print the min and max from a list given 2,3,1,23,5,45,657,23,23,12


def min_max_of_list():
    list = [2,3,1,23,5,45,657,23,23,12]

    return min(list),max(list)    
print("Min",min_max_of_list()[0])
print("Max",min_max_of_list()[1])