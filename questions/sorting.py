from functools import reduce

l=[5,3,8,6,7,2]
even=list(filter(lambda a:a%2==0,l))
print(even)
double=list(map(lambda a:a*10,l))
print(double)

reduce_s=reduce(lambda x,y :x+y,l)
print(reduce_s)