def longest(nums):
    if not nums:
        return 0
    nums = set(nums)
    longest = 0 
    for num in nums:
        if num - 1 not in nums:
            current_num = num
            current_length = 1
            while current_num + 1 in nums:
                current_num += 1
                current_length += 1
            longest = max(longest, current_length)
        return longest

print(longest([100, 4, 200, 1, 3, 2]))
print(longest([0, 0]))
print(longest([9, 1, 4, 7, 3, 2, 8, 5, 6]))