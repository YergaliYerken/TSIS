def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

num_input = input().split()
nums = [int(num) for num in num_input]
print(has_33(nums))
