# 输出倒数第K个元素

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Findkthoftail(self, head, k):
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        if k<0 or k>len(res):
            return False
        return res[-k]