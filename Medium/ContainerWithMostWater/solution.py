# Brute force cannot pass the OJ
def max_area(height):
    last = height[-1]
    length = len(height)
    max_a = 0
    for indi, i in enumerate(height):
        for indj, j in enumerate(range(indi + 1, length)):
            end_h = height[j]
            l = indj + 1
            h = min(i, end_h)
            area = l * h
            max_a = area if area > max_a else max_a

    return max_a

# Actually, the max area of one line x from left is detemined by the first one line y from right who exceeds x, because the max area is defined 
# by the lower line and the distance.
def optimal(height):
    first = 0
    last = len(height) - 1
    max_a = 0
    while first != last:
        max_a = max(max_a, (last - first) * min(height[first], height[last]))
        if height[first] < height[last]:
            first += 1
        else:
            last -= 1
    return max_a

if __name__ == '__main__':
    test_data = [[1,8,6,2,5,4,8,3,7], [1, 2], [1, 2, 3]]
    for i in test_data:
        print(optimal(i))


