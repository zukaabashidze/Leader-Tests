def sum_positive(num):
    return sum(s for s in num if s > 0)

print(sum_positive([1, -4, 7, 12]))
print(sum_positive([-1, -2, -3, -4]))
print(sum_positive([]))
print(sum_positive([1, 2, 3, 4]))