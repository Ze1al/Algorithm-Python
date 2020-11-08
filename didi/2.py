# 5 10000 1000
# 1 5 4 2 3
# 5 4 3 2 1

# 输出 3

import sys

def min_cost_of_arr(arr):
    stack = []
    pass





if __name__ == "__main__":
    strList = []
    for line in sys.stdin:  #当没有接受到输入结束信号就一直遍历每一行
        tempStr = line.split()#对字符串利用空字符进行切片
        tempStr = [int(i) for i in tempStr]
        strList.append(tempStr)#把每行的字符串合成到列表
    print(len(strList))

