def majority_element(nums):
    from math import ceil
    d = {}
    l = len(nums)
    for i in nums:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
        if d[i] >= ceil(l/2):
            return i

if __name__ == '__main__':
    data = [
        [3, 2, 3],
        [1, 1, 2, 2, 1, 1],
        [1],
        [1, 2, 3, 1, 2, 1],
    ]
    for i in data:
        print(majority_element(i))
