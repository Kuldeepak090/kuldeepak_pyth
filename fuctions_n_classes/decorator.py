def make_pretty(func):
    def inner():
        print('i am here')
        func()
    return inner

@make_pretty()
def ordinary():
    print("this is ordinary function")  

ordinary()      

