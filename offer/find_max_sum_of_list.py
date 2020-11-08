# 给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

def FindGreatestSumOfSubArray(array):
    max_res = array[0]
    res = array[0]
    for i in range(1, len(array)):
        max_res = max(max_res+array[i], array[i])
        res = max(max_res, res)
    return res


arr = [6, -3, -2, 7, -15, 1, 2, 2]
print(FindGreatestSumOfSubArray(arr))