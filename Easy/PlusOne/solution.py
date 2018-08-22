def plus_one(ele):
    return (ele + 1)//10, (ele + 1)%10

def plus_lst(lst):
    i = lst.pop()
    carry, res = plus_one(i)
    lst.append(res)
    if carry:
        if len(lst) < 2:
            lst.insert(0, carry)
        else:
            lst = plus_lst(lst[:-1])
            lst.append(res)
    return lst

if __name__ == '__main__':
    data = [
        [0],
        [1],
        [1, 2],
        [1, 2, 3],
        [9],
        [9, 9],
        [9, 9, 9],
        [1, 2, 3, 4],
        [9, 9, 9, 9]
    ]

    for d in data:
        print(d)
        print(plus_lst(d))
        print('')
