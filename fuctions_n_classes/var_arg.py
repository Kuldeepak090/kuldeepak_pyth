def avg(*values):
    return sum(values)/ len(values)

def voewl_counter(vowel_counter, *words):
    c =0
    for word in words:
        vc= word.casefold.count(vowel_char)
        c +=vc
    return c
# com 
   

count = voewl_counter("a", "apple","banana")    
print(" a found", count, "times")

 #print(avg(1,2,3,3,123,13,12,33)) 
#print(avg(1,12,3))   