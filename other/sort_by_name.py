# 输入包括多行，每一行代表一个姓和名字
# 输出排好序以后的名字

from collections import Counter
import sys

names = ['ZHANG SAN', 'LI SI', 'WANG WU', 'WANG LIU', 'WANG QI', 'ZHANG WU', 'LI WU' ]

def get_count(name):
    first_names = [name.split()[0] for name in names]
    first_name = name.split()[0]
    counters = Counter(first_names)
    return counters.get(first_name)

results = sorted(names, key=lambda x: get_count(x), reverse=True)

for result in results:
    print(result)


# if __name__ == "__main__":
#     strList = []
#     for line in sys.stdin:  #当没有接受到输入结束信号就一直遍历每一行
#         tempStr = line.split()#对字符串利用空字符进行切片
#         strList.extend(tempStr)#把每行的字符串合成到列表