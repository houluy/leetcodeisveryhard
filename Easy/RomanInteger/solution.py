'''
My solution
'''
def romantoint(s):
    romanlist = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    num = 0
    it = 0
    slen = len(s)
    while it < slen:
        try:
            double = s[it] + s[it + 1]
        except IndexError:
            num += romanlist.get(s[it])
            return num
        else:
            if double in romanlist:
                num += romanlist.get(double)
                it += 2
            else:
                num += romanlist.get(s[it])
                it += 1
    return num

# -----------Simple tests here-----------------
slist = [
    'III',
    'XI',
    'VI',
    'IV',
    'IX',
    'LVIII',
    'MCMXCIV',
    'XXI',
    'CII',
    'CXI',
    'MDCLXVI',
]

for s in slist:
    print(s, end='')
    print(romantoint(s))
