#### take a user input and store the values in list, till the user enters eof

def a():
  x = []
  while True:
    data = input("enter anything: ")
    if data.casefold() == "eof'":
      break
  else:
    x.append(data)
print(a())    