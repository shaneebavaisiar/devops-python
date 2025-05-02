# Implement a binary search on a sorted list.
l = [1, 2, 3, 4, 5, 6, 7, 9]
target = 7
left = 0
right = len(l) - 1

while left <= right:
    mid_value = (left + right) // 2
    if l[mid_value] == target:
        print(f"target value in {mid_value} index")
        break
    elif l[mid_value] < target:
        left = mid_value + 1
    else:
        right = mid_value - 1
else:
    print("target not found")
