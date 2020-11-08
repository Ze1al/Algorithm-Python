# 输入一个链表，输出该链表中倒数第k个结点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def FindKthToTail(head, k):
    if head==None or k == 0:
        return None
    p1 = head
    p2 = head
# p1先走k步，然后p2开始移动，则是倒数k个节点
    while k-1>0:
        if p1.next != None:
            p1 = p1.next
            k-=1
        else:
            return None
    while p1.next != None:
        p1 = p1.next
        p2 = p2.next
    return p2


