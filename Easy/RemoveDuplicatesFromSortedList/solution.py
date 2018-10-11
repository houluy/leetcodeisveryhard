import pdb
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    #pdb.set_trace()
    start = current = head
    try:
        head = head.next
    except:
        return head
    while head:
        if current.val != head.val:
            current.next = head
            current = current.next
        head = head.next
    current.next = head
    return start

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(2)
l5 = ListNode(3)
l6 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

L = deleteDuplicates(l1)

while L:
    print(L.val)
    L = L.next
