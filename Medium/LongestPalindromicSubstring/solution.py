def expand(s, left, right, l):
    while True:
        if left >= 0 and right < l and s[left] == s[right]:
            left -= 1
            right += 1
        else:
            break
    return right - left + 1

def palindromic(s):
    l = len(s)
    if l == 0:
        return ""
    start = end = 0
    for i in range(l):
        l1 = expand(s, i, i, l)
        l2 = expand(s, i, i + 1, l)
        ml = max(l1, l2)
        if (ml > end - start):
            start = i - (ml - 1)//2
            end = i + (ml + 1)//2
        print(start, end)
    return s[start:end + 1]

if __name__ == '__main__':
    test_data = ['baba', '', 'cbbd', 'cbbc', 'abcddddddddcba']
    for i in test_data:
        print(palindromic(i))

