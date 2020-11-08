# 二叉树的广度遍历

class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        sol = []
        curr = root
        queue = [curr] # 队列
        while queue:
            curr = queue.pop(0)
            sol.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return sol