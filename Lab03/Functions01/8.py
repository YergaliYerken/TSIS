def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2] == 7:
            return True
    return False

num_input = input().split()
nums = [int(num) for num in num_input]
print(has_33(nums))
