
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

# 后序遍历 左右中  二叉搜索树 左边最小  中间  右边最大

def VerifySquenceOfBST(sequence):
    n = len(sequence)
    if n == 0:
        return False
    if n == 1:
        return True
    root = sequence[-1]
    left = 0
    while sequence[left] < root:
        left += 1
    for i in range(left, n-1):
        if sequence[i] < root:
            return False
    return VerifySquenceOfBST(sequence[:left]) or VerifySquenceOfBST(sequence[left:n-1])