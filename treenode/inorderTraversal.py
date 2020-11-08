# 中序遍历的递归版本

class TreeNode:
    def __init__(self, x):
        self.val =x
        self.left = None
        self.right = None

def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.left)
