# Create a dictionary from two lists:
keys = ["name", "age", "city"]
values = ["Ashu", 28, "Delhi"]
dic={}
k=0
for i in keys:
    dic[i]=values[k]
    k+=1
print(dic)
