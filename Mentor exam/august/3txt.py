def ajaja_num(num):
    result = []
    num_str = str(num)[::-1]
    for i in range(len(num_str)):
        ak = num_str[i]
        if ak != '0':
            result.append(ak + '0' * i)
    return ' + '.join(result[::-1])

# Test cases
print(ajaja_num(70304))  
print(ajaja_num(42))    
print(ajaja_num(710163)) 
print(ajaja_num(853546)) 
print(ajaja_num(511604)) 