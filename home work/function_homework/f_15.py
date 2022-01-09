## create a dictionary to add 5 employees with details like name, designation, salary , joining data, dept , etc

def k():
    Employees = {}
    for i in range(1,6):
        info = {}
        info["name"] = input("Enter employee name: ")
        info["designation"] = input("Enter employee designation: ")
        info["salary"] = input("Enter employee salary: ")
        info["joining date"] = input("Enter joining date: ")
        Employees[i] = info
    return Employees