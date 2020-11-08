
import sys


def name_ord(list):
    # 输入一个列表
    dict = {}
    n = len(list)
    for i in range(0, n, 2):
        if list(i) not in dict:
            dict[i] = 1
        else:
            dict[i]+=1

    print(dict)



if __name__ == "__main__":
    strList = []
    for line in sys.stdin:  #当没有接受到输入结束信号就一直遍历每一行
        tempStr = line.split()#对字符串利用空字符进行切片
        strList.extend(tempStr)#把每行的字符串合成到列表
    # print(strList)
    arr = ['zhang', 'san', 'li', 'si', 'li', 'wu']
    name_ord(arr)

