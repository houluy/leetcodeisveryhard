def reverse(num):
    rev = 0
    dig = 0
    sign = 1 if num > 0 else -1
    num = abs(num)
    while num:
        dig = num % 10
        low = (-2**31 - dig)//10
        high = (2**31 - 1 - dig)//10
        if low <= rev <= high:
            rev = 10 * rev + dig
        else:
            return 0
        num //= 10
    return rev * sign

if __name__ == '__main__':
    num_lst = [0, 1, -1, 123, -123, -2**31, 2**31-1]
    for i in num_lst:
        print(reverse(i))
    
