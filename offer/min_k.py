# 输入n个整数，找出其中最小的K个数。
# 例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。


def GetLeastNumbers_Solution(tinput, k):
    if not tinput:
        return
    if k>len(tinput):
        return tinput
    tinput.sort()
    return tinput[:k]


print(GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))