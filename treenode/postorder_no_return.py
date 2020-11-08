# 后序遍历的非递归版本
# 左右中    倒着反着实现是 中右左

def postorder(root):
    stack = []
    sol = []
    curr = root
    while stack or curr:
        if curr:
            sol.append(curr.val)
            stack.append(curr.left)
            curr = curr.right
        else:
            curr = stack.pop()
    return sol[::-1]

# 中右左
def _postorder(root):
    stack = []
    res = []
    curr = root
    while stack or curr:
        if curr:
            res.append(curr.val)
            stack.append(curr.left)
            curr = curr.right
        else:
            curr = stack.pop()
    return res[::-1]