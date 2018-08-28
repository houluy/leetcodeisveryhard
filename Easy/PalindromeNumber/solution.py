def is_pa(num):
    if num < 0:
        return False
    rev = 0
    tnum = num
    while num:
        dig = num % 10
        num //= 10
        rev = rev * 10 + dig
    return True if rev == tnum else False

## Half revert to avoid overflow

def half_rev(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    rev = 0
    while num > rev:
        rev = rev * 10 + num % 10
        num //= 10
    if num == rev or num == rev//10:
        return True
    else:
        return False

if __name__ == '__main__':
    test_data = [-121, 121, 0, 1, 10, 1234321]
    #test_data = [10]
    for i in test_data:
        print(i, half_rev(i))
