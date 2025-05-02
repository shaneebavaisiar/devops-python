# Write code to find the second largest number in a list.

lis = [1, 10, 4, 7, 8, 8, 7, 3, 10]
set_li = set(lis)  # to avoid dublicates
sorted_set = sorted(set_li)
second_largest = sorted_set[len(sorted_set) - 2]
print(second_largest)
