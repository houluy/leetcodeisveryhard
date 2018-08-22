def i2r(num):
    s = []
    n2r_dic = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    for base in order:
        roman = n2r_dic[base]
        r = num // base
        if r > 0:
            s.append(roman * r)
            num -= r * base
    return ''.join(s)
    
# Fastest solution
class Solution:
    
    ONE = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    TEN = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    HUN = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    THU = ["", "M", "MM", "MMM"]
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return Solution.THU[num // 1000 % 10] + Solution.HUN[num // 100 % 10] + Solution.TEN[num // 10 % 10] + Solution.ONE[num % 10];

if __name__ == '__main__':
    test_num = list(range(3990, 4000))
    for i in test_num:
        print(i, i2r(i))
