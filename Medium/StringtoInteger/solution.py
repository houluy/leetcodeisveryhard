def atoi(s):
    white = True
    sign = 1
    num = 0
    max_num = 2**31 - 1
    min_num = -2**31
    zero_ord = 48
    for i in s:
        if (i == ' ' and white):
            continue
        elif i == '+' and white:
            white = False
            continue
        elif i == '-' and white:
            white = False
            sign = -1
            continue
        else:
            ascii_num = ord(i) - zero_ord
            if 0 <= ascii_num <= 9:
                num = num * 10 + ascii_num
                if (num*sign < min_num):
                    return min_num
                elif (max_num < num*sign):
                    return max_num
                white = False
            else:
                break
    num *= sign
    return num

if __name__ == '__main__':
    test_data = ['  -21', '123', 'abcd123', '    ', '', '  -02abcd', '12 34', '12345678901902', '-91283472332', '0', '1', '4193 with words', 'words and 987']
    test_data = ['+-1']
    for i in test_data:
        print(i, atoi(i))
