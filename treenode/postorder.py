# 后序遍历 非递归版本
# 左 右 中
def postorderTraversal(root):
    if not root:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]

