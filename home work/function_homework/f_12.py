#### Calculate the sum of the values in tyhe list ['$100' , '$200', '$230', $'120', '$240']

def h():
    a_list = ['$100', "$200", "$230", "$120", "$240"]
    result = map(lambda i: int(i[1:]), a_list)
    return sum(result)
print(h())