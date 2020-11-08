# 检查是否有循环链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hascyclelistnode(self, pHead):
        slowptr= pHead
        fastptr = pHead
        biaozhi = False

        if pHead == None:
            return True
        while fastptr.next != None and fastptr.next.next != None:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if slowptr == fastptr:
                print("存在环结构")
                biaozhi = True
                break

            else:
                print("不存在环结构")



