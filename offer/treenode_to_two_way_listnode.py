
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TwoWayList:
    def __init__(self, x):
        self.val = x
        self.pre = None
        self.next = None



# 二叉搜索树， 左中右， 中序遍历

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        
        stack = []
        p = pRootOfTree
        res = []
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right

        resP = res[0]
        while res:
            top = res.pop(0)
            if res:
                top.right = res[0]
                res[0].left = top
        return resP







