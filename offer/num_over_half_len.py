# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

def MoreThanHalfNum_Solution(numbers):
    list = [i for i in numbers]
    n = len(list)
    dict = {}
    for i in list:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for j in dict:
        if dict[j] > n/2:
            return j
    else:
        return 0

print(MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))