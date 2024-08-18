def cakes(r, a):
    max = float('inf')
    for ing, amount in r.items():
        if ing in a:
            max = min(max, a[ing] // amount)
        else:
            return 0
    return max