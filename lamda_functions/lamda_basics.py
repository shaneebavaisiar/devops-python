lis=[1,4,6,7,8]
x=list(filter(lambda a:a%2==0,lis))
print(x)

a,b=3,5
x=lambda a,b:a+b
print((lambda a,b:a+b)(a,b))