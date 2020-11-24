# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
    复杂链表的复制
    思路：将原来的链表进行复制，最后拆开
"""

class Node():
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        # 复制节点拼接
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = cur.next.next

        # 复制random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 拆开
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res







