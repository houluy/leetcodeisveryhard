import pdb
def maxProfit(prices):
    total = 0
    l = len(prices)
    current = 0
    endind = 0
    try:
        price = prices[endind]
    except IndexError:
        return total
    last = price
    endind += 1
    while endind < l:
        end = prices[endind]
        if end < last:
            price = prices[endind]
            total += current
            current = 0
        else:
            cp = end - price
            if current < cp:
                current = cp
        last = end
        endind += 1
    total += current
    return total

test = [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1], [10000 - x for x in range(10000)]]
for i in test:
    print(maxProfit(i))
