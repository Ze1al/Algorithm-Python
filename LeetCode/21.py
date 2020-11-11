# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
合并两个有序列表
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 定义新的链表
        newListNoneHead = ListNode(0)
        cur = newListNoneHead  # 当前指针

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if not l2 else l2
        return newListNoneHead.next











