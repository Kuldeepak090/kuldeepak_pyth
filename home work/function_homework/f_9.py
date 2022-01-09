### Create a list of 10 fruits , then generaye a list of fruits using comprehension the contain 6 or less characters

def e():
    fruits = ["apple", "banana", "orange", "pomegrenate", "mango", "dragonfruit", "pear", "kiwi", "guava", "grapes"]
    fruits2 = list(i for i in fruits if len(i) <= 6)
    return fruits2
print(e())