# count the sum of words with limited num of chars
def word_counter(msg,limit):
    words = msg.split()
    wl = []
    for items in words:
        if len(items) == limit:
            wl.append(items)
    return len(wl)

data = '''the author who
 has a made '''  
print("4 letter word count is",word_counter(data,limit =10))           
