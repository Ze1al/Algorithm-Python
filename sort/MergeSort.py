# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""


# 先拆分，之后再和回去
# 归并排序，分而治之

def Merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_arr_set = Merge(left)
    right_arr_set = Merge(right)
    return mergeSort(left_arr_set, right_arr_set)


def mergeSort(leftArr, rightArr):
    arrNew = []
    i = j = 0 # 指针
    while i<len(leftArr) or j<len(rightArr):
        if leftArr[i] and rightArr[j]:
            if leftArr[i] < rightArr[j]:
                arrNew.append(leftArr[i])
            if leftArr[i] >= rightArr[j]:
                arrNew.append(rightArr[j])
        if not leftArr[i]:
            arrNew.extend(rightArr[j:])
        if not rightArr[j]:
            arrNew.extend(leftArr[i:])
    return arrNew



