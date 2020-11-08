
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。


import itertools

def Permutation(ss):
    # write code here
    if not ss:
        return []
    tmp = []
    a = itertools.permutations(ss)
    for i in a:
        print(i)
        tmp.append(i)

    b = map(''.join, a)
    c = set(b)
    d = list(c)
    e = sorted(d)
    return e

if __name__ == '__main__':
    print(Permutation('abc'))

