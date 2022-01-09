def avg(*values):
    return sum(values)/ len(values)

def vowel_counter(vowel_char, *words):
    c =0
    for word in words:
        vc= word.casefold().count(vowel_char)
        c +=vc
    return c

   
# comprehension

def vowel_counter_comp(vowel_char , *words):
    return sum([word.casefold().count(vowel_char) for word in words])

 #print(avg(1,2,3,3,123,13,12,33)) 
#print(avg(1,12,3))   

count = vowel_counter('a','apple','banana','cherry','japan')
print("A found", count , "times")
count = vowel_counter_comp('e','apple','banana','cherry','japan')
print("E found",count,"times")