# 前序遍历 非递归版本
# 中 左 右

def preorder(root):
    stack = []
    sol = []
    curr = root
    while stack or curr:
        if curr:
            sol.append(curr.val)
            stack.append(curr.right)    # 右节点压入栈中
            curr = curr.left            # 指针往左边走
        else:
            curr = stack.pop()
    return sol