# 广度遍历的非递归版本

def levelorder(root):
    if not root:
        return []
    sol = []
    curr = root
    queue = [root]  # 队列
    while queue:
        curr = queue.pop(0)
        sol.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return sol

