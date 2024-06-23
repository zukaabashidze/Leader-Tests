def valid_ISBN10(isbn):
    # Check format
    if len(isbn) != 10 or not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    # Check modulo
    return sum(i*(10 if x=='X' else int(x)) for i,x in enumerate(isbn, 1)) % 11 == 0