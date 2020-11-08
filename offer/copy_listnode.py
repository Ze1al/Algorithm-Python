# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
# 返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

    # 首先尝试复制节点
        p = pHead
        while p:
            p_next = p.next
            copy_node = ListNode(p.val)    # 拷贝的节点
            p.next = copy_node
            copy_node.next = p_next
            p = p.next

    # 拷贝随机指针
        p = pHead
        while p:
            p_random = p.random
            copy_node = p.next
            if p_random:
                copy_node.random = p_random.next
            p = p.next.next

    # 拆解出两条链表
        p = pHead
        copy_p = pHead.next
        while p:
            copy_node = p.next   # 拷贝的节点
            p_next = copy_node.next   # 原来的next节点
            p.next = p_next
            if copy_node:
                copy_p.next = p_next.next
            else:
                copy_p.next = None

        return copy_p






