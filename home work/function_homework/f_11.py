#### Create a list 10 words and then extract all the words starting with letter A OR a using map.

def g():
    words = ["apple", "banana", "orange", "pomegrenate", "mango", "dragonfruit", "pear", "kiwi", "guava", "grapes"]
    words2 = list(i for i in words if i.startswith('a') or i.startswith('A'))
    return words2
print(g())