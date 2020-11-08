# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def Convert(pRootOfTree):
    if not pRootOfTree:
        return pRootOfTree
