# Write a function to flatten a nested list.
li = [[1, 2, 3], [8, 10, 3], [9, 5, 0],10,3,"string"]

flatten_list=[]
for i in li:
    if type(i)==list:
        for j in i:
            flatten_list.append(j)
    else:
        flatten_list.append(i)
print(flatten_list)
