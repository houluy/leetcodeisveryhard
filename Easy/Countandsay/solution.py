# Count and say
# Using groupby in itertools
# A little tricky
#
from itertools import groupby
def countandsay(c):
    def say(last):
        retstr = ''
        for val, group in groupby(last):
            retstr += '{}{}'.format(len(list(group)), val)
        return retstr
    for i in range(c):
        if i == 0:
            n = '1'
        else:
            n = say(n)
    return n
