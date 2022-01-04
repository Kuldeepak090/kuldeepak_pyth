def totavg():
   x = list(range(1,50))
   total =sum(x)
   avg= total/len(x)
   return total,avg

t,a =totavg()
print(f'the total is {t} and average is {a}')   
