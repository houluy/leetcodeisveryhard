import pdb
def maxProfit(prices):
    mp = 0
    l = len(prices)
    nind = 0
    while nind < l:
        price = prices[nind]
        endind = nind + 1
        while endind < l:
            end = prices[endind]
            if end < price:
                nind += 1
                price = prices[nind]
                endind += 1
                continue
            cp = end - price
            if mp < cp:
                mp = cp
            endind += 1
        else:
            return mp
    return mp

test = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [10000 - x for x in range(10000)]]
for i in test:
    print(maxProfit(i))
