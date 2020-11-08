# 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

def FindPath(root, expectNumber):
    if not root:
        return []
    tmp = []
    if not root.left and not root.right and expectNumber==root.val:
        return [root.val]
    else:
        left = FindPath(root.left, expectNumber-root.val)
        right = FindPath(root.right, expectNumber-root.val)
        for item in left+right:
            tmp.append([root.val]+item)
        return tmp
