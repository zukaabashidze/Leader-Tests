# 1)  (2 ქულა)
#
def demic(Binary_str):
    return int(Binary_str, 2)

# Testcases:

print(demic("10001"))
print(demic("1111"))



# 2) (2 ქულა)

def demic(num):
    if num == 0:
        return "0"
    Binary_s = ""
    while num > 0:
        Binary_s = str(num % 2) + Binary_s
        num = int(num / 2)
    return Binary_s



# Testcases:

print(demic(15)) # 1111
print(demic(17)) # 10001

# 3) (3 ქულა)

def remove_duplic(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result

print(remove_duplic([1, 2, 2, 3, 4, 4, 5])) # [1, 2, 3, 4, 5]
print(remove_duplic(['a', 'b', 'a', 'c'])) # ['a', 'b', 'c']

# 4) (3 ქულა)

def fac(n):
    if n == 0:
        return 1
    total = 1
    for s in range(1, n + 1):
        total *= s
    return total

print(fac(5))
print(fac(0))

# 5)  (3 ქულა)

def palindrome(i):
    space = ""
    for s in i:
        if ('a' <= s.lower() <= 'z'):
            space += s.lower()

    return space == space[:: -1]
 
print(palindrome("A man a plan a canal Panama")) #True
print(palindrome("Hello")) # False 

# 6)  (4 ქულა)
def pascal(k):
    snake = ""
    for i in k:
        if i.isupper() and snake:
            snake += '_'
        snake += i.lower()
    return snake

print(pascal("TestController"))
print(pascal("MoviesAndBooks"))
print(pascal("App7Test"))
print(pascal("1"))
# 7) (4 ქულა)

def fibonaci(n):
    last = []
    a, b = 0, 1
    for i in range(n):
        last.append(a)
        a, b = b, a + b
    return last

print(fibonaci(5))
print(fibonaci(7))

# 8) (4 ქულა)

def sort(st):
    words = st.split()
    
    sort_wrd = [''] * (len(words) + 1)  
    
    for word in words:

        dolce = ""
        for char in word:
            if char.isdigit():
                dolce += char  
        
        if dolce: 
            index = int(dolce) 
            sort_wrd[index] = word 
    
    return ' '.join(sort_wrd[1:])

# Test Cases
print(sort("is2 Thi1s T4est 3a"))  # --> "Thi1s is2 3a T4est"
print(sort("4of Fo1r pe6ople g3ood th5e the2"))  # --> "Fo1r the2 g3ood 4of th5e pe6ople"
print(sort(""))  # --> ""





# 9) (4 ქულა)

def prime(max):
    primo = []
    for num in range(2, max + 1):
        for i in range(2, int(num *.5) + 1):
            if num % i == 0:
                break
        else:
            primo.append(num)
    return primo

print(prime(11)) # [2, 3, 5, 7, 11]





# 10) (5 ქულა)
def erueka(a, b):
    eureka_lst = []
    for num in range(a, b + 1):
        digits = [int(d) for d in str(num)]
        sum = 0
        for i in range(len(digits)):
            sum += digits[i] ** (i + 1)

        if sum == num:
            eureka_lst.append(num)
    return eureka_lst
print(erueka(1, 10))
print(erueka(1, 100))