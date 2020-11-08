# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Merge(pHead1, pHead2):
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1
    pMergeListNode = None
    if pHead1.val < pHead2.val:
        pMergeListNode = pHead1
        pMergeListNode.next = Merge(pMergeListNode, pHead2)
    else:
        pMergeListNode = pHead2
        pMergeListNode.next = Merge(pHead1, pHead2.next)
    pMergeListNode = pMergeListNode.next
    return pMergeListNode
