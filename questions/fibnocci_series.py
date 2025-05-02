# fib=0,1,1,2,3,5,8
# n=7
# a=0
# b=1
# if n==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         print(c)
#         a=b
#         b=c


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=4
for i in range(4):
    print(fibonacci(i))


