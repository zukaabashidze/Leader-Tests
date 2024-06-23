def capitalize(s):
    even_capitalize = ""
    odd_capitalize = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even_capitalize += s[i].upper()
            odd_capitalize += s[i]
        else:
            even_capitalize += s[i]
            odd_capitalize += s[i].upper()
            
    return [even_capitalize , odd_capitalize]
#7kyu