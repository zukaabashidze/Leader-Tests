def check(arr):
    if not arr:  
        return True
    
    for kata in arr:
        if isinstance(kata, (int, float)): 
            if isinstance(kata, float) and not kata.is_integer():  
                return False
        else:
            return False
    
    return True

# test case
print([])
print([  1, 2, 3, 4])
print([1.0, 2.0, 3.0])
print([1.0, 2.0, 3.0001]) 
print(["-1"]) 
