def climbStairs(n):
    '''
    This is just a Fibonacci Sequence
    '''
    def climb(last):
        a, b = 1, 2
        while last:
            yield a
            a, b = b, a + b
            last -= 1
    i = 0
    for i in climb(n):
        pass
    return i
nums = [1, 2, 3, 4, 5, 6]
for t in nums:
    print(climbStairs(t))
