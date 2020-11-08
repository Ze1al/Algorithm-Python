# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

# 前序遍历 中左右   后序遍历 左右中
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

def reConstructBinaryTree(pre, tin):
    if not len(pre):
        return 0
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        root = pre[0]
        root.left = reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
        root.right = reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
    return root


