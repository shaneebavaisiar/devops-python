l = [1, 2, 3, 4, 5, 6, 7, 9]
target = 10
left=0
right=len(l)-1
while left<=right:
    mid=(left+right)//2
    if l[mid]==target:
        print(f"target value found at index {mid}")
        break
    elif l[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("value not found !!!")



