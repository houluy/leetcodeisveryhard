def length(s):
    white = ' '
    end = False
    length = 0
    for i in reversed(s):
        if i == white and end:
            return length
        elif i != white:
            length += 1
            end = True
    return length

if __name__ == '__main__':
    test_data = ['hello world', '', '   ', 'i     ', 'please help me   ']
    for i in test_data:
        print(i, length(i))
