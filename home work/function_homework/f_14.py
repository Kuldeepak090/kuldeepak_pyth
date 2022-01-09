## create a dictionary that contains prices of common items and then write the code to display the sum and avg price of all items.


def j():
    total = 0
    common_items = {'fruits':'100', 'Chips':'15', 'Carrots':'40', 'Biscuits':'20'}
    for item in common_items:
        total+=int(common_items.get(item))
        average = total/len(common_items)
    return total,average
print("Total",j()[0])
print("Average",j()[1])