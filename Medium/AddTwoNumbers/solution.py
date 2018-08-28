class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two(l1, l2):
    start = None
    carry = 0
    while True:
        l1end = l1 is None
        l2end = l2 is None
        if l1end and l2end:
            if carry:
                pointer.next = ListNode(carry)
            return start
        else:
            if l1end:
                l1 = ListNode(0)
            elif l2end:
                l2 = ListNode(0)
            carry, res = divmod(l1.val + l2.val + carry, 10)
            if start is None:
                start = ListNode(res)
                pointer = start
            else:
                pointer.next = ListNode(res)
                pointer = pointer.next
            l1, l2 = l1.next, l2.next
    return start 

def print_list(l):
    s = []
    while l:
        s.append(l.val)
        l = l.next
    return s

if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)

    r1 = ListNode(5)
    r2 = ListNode(6)
    r3 = ListNode(4)
    l1.next = l2
    l2.next = l3
    r1.next = r2
    r2.next = r3

    #l1 = ListNode(0)
    #r1 = ListNode(9)

    #l1 = ListNode(1)
    #r1 = ListNode(9)

    l1 = ListNode(9)
    l2 = ListNode(9)
    l3 = ListNode(9)
    r1 = ListNode(1)
    l1.next = l2
    l2.next = l3

    print(print_list(add_two(l1, r1)))
