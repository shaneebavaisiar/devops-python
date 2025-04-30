# Write a program to count the frequency of each word in this list:
l=["apple", "banana", "apple", "orange", "banana", "apple"]
dic={}
for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
