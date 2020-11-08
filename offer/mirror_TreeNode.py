
#  操作给定的二叉树，将其变换为源二叉树的镜像。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def Mirror(root):
    if not root:
        return root
    if not root.right and not root.left:
        return root
    if not root.right or not root.left:
        tmp = root.right
        root.left = root.right
        root.right = tmp
    Mirror(root.left)
    Mirror(root.right)
    return root


