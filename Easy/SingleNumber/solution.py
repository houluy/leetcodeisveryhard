# My Solution
def single_number(lst):
    d = {}
    for i in lst:
        if i in d:
            d.pop(i)
        else:
            d[i] = 0
    return list(d.keys())[0]

# Solutions by others
# Use XOR operations
def single(lst):
    from functools import reduce
    from operator import xor
    return reduce(xor, lst)

if __name__ == '__main__':
    test_data = [
        [2, 2, 1],
        [4, 2, 2, 1, 1],
        [1],
    ]
    for t in test_data:
        print(single_number(t))
        print(single(t))
