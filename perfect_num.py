def is_perfect_num(num):
    total = 1
    ls = []
    if num <= 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            total += i
    
    if total == num:
        return True
    return False

print(is_perfect_num(496))