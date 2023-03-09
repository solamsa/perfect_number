def is_perfect_num(num):
    """arguments:   Function take the number to be checked
                    if it is a perferct or not
        returns: (boolean) true if it is perfect else false"""
    total = 1
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            total += i
    if total == num:
        return True
    return False

print(is_perfect_num(496))