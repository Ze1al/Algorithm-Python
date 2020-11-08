# 在一个字符串中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写)


def FirstNotRepeatingChar(s):
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for j in s:
        if dict[j] == 1:
            return s.find(j)

