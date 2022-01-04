def word_count(message):
    return len(message.split())

data = "hi everyone"
print(word_count(data))  

data = "this is easy"
print(word_count(data))

print(word_count('hey now'))