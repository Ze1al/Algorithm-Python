# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

# 二叉树的中序遍历
# 左中右

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        if not root:
            return None
        stack = []       # 维护一个栈
        res = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res














