#交叉链表求交点

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
def node(l1,l2):
    lenth1,lenth2 = 0,0
    while l1.next:
        l1 = l1.next
        lenth1 += 1
    while l2.next:
        l2 = l2.next
        lenth2 += 1
    if lenth1 > lenth2:
        for _ in range(lenth1 - lenth2):
            l1 = l1.next
    else:
        for _ in range(lenth1 - lenth2):
            l2 = l2.next
    while l1 and l2:
        if l1.next == l2.next:
            return l1.next
        else:
            l1 = l1.next
            l2 = l2.next
