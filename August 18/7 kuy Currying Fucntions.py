def multiply_all(arr):
    def multiply(s):
        result = []
        for g in range(0, len(arr)):
            aka = arr[g]*s
            result.append(aka)
            
        return result
    return multiply