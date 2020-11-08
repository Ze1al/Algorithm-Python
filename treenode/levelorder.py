# 广度优先遍历

def levelorder(root):
    sol = [[]]
    def helper(node, level):   # level表示当前节点的层数
        if not node:
            return
        else:
            sol[level-1].append(node.val)
            if len(sol) == level:   # 遍历到新层时，只有最左边的结点使得等式成立
                sol.append([])
            helper(node.left, level+1)
            helper(node.right, level+1)
    helper(root, 1)
    return sol[::-1]