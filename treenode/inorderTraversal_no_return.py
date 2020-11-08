# 中序遍历的非递归版本
# 中序遍历的顺序是   左 中 右

def inorderTraversal_no_return(root):
    stack = []   # 二叉树遍历一半都要使用栈这个结构
    sol = []
    curr =root
    while stack or curr:   # 栈为空或者指针为None
        if curr:
            stack.append(curr)    # 中间节点压入栈中
            curr = curr.left      # 指针往左边走
        else:
            curr = stack.pop()    # 弹出当前节点
            sol.append(curr.val)  # 添加当前值
            curr = curr.right
    return sol

