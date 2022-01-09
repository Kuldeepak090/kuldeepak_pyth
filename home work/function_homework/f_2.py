### WAP to print average of a list given below 12,1,23,34,45,56,23,12


def average_of_list():
    list = [12,1,23,34,45,56,23,12]
    total = 0

    for number in list:
        total += number
    
    return total, total/len(list)

print("Total ",average_of_list()[0] ,average_of_list()[1])