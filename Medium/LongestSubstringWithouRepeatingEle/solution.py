def longest_substring(s):
    i = 0
    j = 0
    ch_ind = {}
    slen = len(s)
    if not slen:
        return slen
    ll = 1
    for j in range(slen):
        c = s[j]
        if c in ch_ind and ch_ind[c] >= i:
            sub_len = j - i
            if sub_len > ll:
                ll = sub_len
            i = ch_ind[c] + 1
        ch_ind[c] = j
    else:
        sub_len = j - i + 1
        if sub_len > ll:
            ll = sub_len
    return ll

if __name__ == '__main__':
    test_data = ['abcda', 'abababcdd', 'dddddd', 'abcdefghigkg', 'pwwkew', 'a', 'aa', 'ab', 'abc', 'aba', 'abcdefghijklmnopqrst', '', 'dvdf']
    #test_data = ['aa']
    for i in test_data:
        print(i, longest_substring(i))
