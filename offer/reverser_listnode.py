# 翻转链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverserListNode(self, pHead):
        if not pHead or not pHead.next:
            return None

        Node = None
        while pHead:
            p = pHead
            pHead = pHead.next
            p.next = Node
            Node = p
        return Node


