def hammingWeight(n):
    num = 0
    while True:
        if (n % 2):
            num += 1
        n >>= 1
        if not n:
            break
    return num

# Bit Manipulation Trick
def trick(n):
    num = 0
    while n:
        num += 1
        n &= (n - 1)
    return num

if __name__ == '__main__':
    test_data = [0, 1, 2, 3, 4, 5, 11, 111111111]
    for d in test_data:
        print('{:b}: {}, {}'.format(d, hammingWeight(d), trick(d)))
