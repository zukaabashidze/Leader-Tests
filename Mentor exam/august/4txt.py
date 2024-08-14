def sort_num(num):
    odd_nums = [n for n in num if n % 2 != 0]
    even_nums = [n for n in num if n % 2 == 0]

    if len(odd_nums) == 1:
        return odd_nums[0]
    else:
        return even_nums[0]

print(sort_num(["2, 4, 0, 100, 4, 11, 2602, 36"]))
print(sort_num(["160, 3, 1719, 19, 11, 13, -21"]))
print(sort_num(["7516484, 526386, 1637037, 813302, -8496994, 812820, 3797630, -3773758, 921354, 6123650, 1693668"]))
print(sort_num(["8811272, 9218790, 9094178, -818772, 2711934, -3905606, 1332109"]))
print(sort_num(["-4207752, 362590, 5205484, 11340, 3740336, 1360605"]))
