def histogram(nums):
    for num in nums:
        print('*' * num)

nums_input = input()
nums = [int(num) for num in nums_input.split()]
histogram(nums)
