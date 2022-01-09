## WAP to take input from user 10 times and the calculate and average

def total_and_average():
    total = 0
    for i in range(10):
        total += int(input("Enter a number: "))
    return total

total1 = total_and_average()
print("Total",total1)
print("Average",total1/10)