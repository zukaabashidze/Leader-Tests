# Determine if a walk (given as an array of directions) takes exactly 10 minutes 
# and returns you to the starting point.

# Args:
# walk (list of str): List of one-letter direction strings ('n', 's', 'e', 'w').
# Each direction takes 1 minute (so list with length of 10 elements takes 10 minutes)

# Returns:
# bool: True if the walk is exactly 10 minutes and returns to start, False otherwise.

# Test Cases:
# ['w','e','w','e','w','e','w','e','w','e','w','e'] -> False
# ['n','s','n','s','n','s','n','s','n','s'] -> True
# ['n','n','n','s','n','s','n','s','n','s'] -> False
# ['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] -> False
# ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] -> True


def determine_walk(siaruli):

    x, y = 0, 0
    

    for a in siaruli:
        if a == 'n':
            y += 1
        elif a == 's':
            y -= 1
        elif a == 'e':
            x += 1
        elif a == 'w':
            x -= 1
    

    return x == 0 and y == 0 and len(siaruli) == 10


print(determine_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))  # False
print(determine_walk(['n','s','n','s','n','s','n','s','n','s']))  # True
print(determine_walk(['n','n','n','s','n','s','n','s','n','s']))  # False
print(determine_walk(['e', 'e', 'w', 'n', 'n','s', 'e', 'w', 'n','s']))  # False
print(determine_walk(['e', 'w', 'e', 'w', 'n','s', 'n','s', 'e', 'w']))  # True


