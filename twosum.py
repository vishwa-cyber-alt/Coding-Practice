nums = [2, 7, 11, 15]
target = 18

for i in range(len(nums)):
    for j in range(i+1, len(nums)): 
        if nums[i] + nums[j] == target:
            print("Indices:", i, j)
            print("Numbers:", nums[i], nums[j])
            print("Sum:", nums[i] + nums[j])
