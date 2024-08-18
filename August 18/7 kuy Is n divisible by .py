def is_divisible(n, *args):
    if not args:
        return True
    return all(n % arg == 0 for arg in args)