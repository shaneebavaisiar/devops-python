import sys
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

a=float(sys.argv[1])
operation=sys.argv[2]
b=float(sys.argv[3])

if operation=="add":
    out=add(a,b)
    print(out)
if operation=="sub":
    out=sub(a,b)
    print(out)