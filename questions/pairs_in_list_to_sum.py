# Find all pairs in a list that sum to a specific target.

nums = [2, 4, 3, 5, 7, 8, 1, 9]

target = 10

for i in range(len(nums)):
    for j in nums[i+1:]:
        if nums[i]+j==10:
            print((nums[i],j))
