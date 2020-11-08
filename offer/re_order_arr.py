# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

def reorderarr(arr):
    res_left = []
    res_right = []
    for i in arr:
        if i%2 == 0:
            res_left.append(i)
        if i%2 == 1:
            res_right.append(i)

    res_left.extend(res_right)
    return res_left


if __name__ == '__main__':
    arr = [4, 5, 32, 1, 2, 31, 3]
    print(reorderarr(arr))