def missing_number(numbers):
    n = len(numbers) + 1
    if len(numbers) == 1 and 1 not in numbers:
        return []
    exp_sum = n * (n + 1) // 2
    act_sum= sum(numbers)
    return exp_sum - act_sum
print(missing_number([1, 2, 4, 5]))
print(missing_number([3, 5, 6, 1, 2]))
print(missing_number([2]))