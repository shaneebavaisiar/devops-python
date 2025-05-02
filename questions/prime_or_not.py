#prime_numbers=2,3,5,7,11

n = 2
for i in range(2, n):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")
