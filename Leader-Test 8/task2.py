def sum_positive(numbers):
    return sum(int(num) for num in numbers if num > 0)

print(sum_positive([1, -4, 7, 12])) 
print(sum_positive([-1.5, 2.7, -3.3, 4.8])) 
print(sum_positive([])) 
print(sum_positive([-1, -2, -3])) 