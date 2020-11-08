# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。


def Permutation(ss):
    if len(ss)<0:
        return []
    res = []
    perm(ss,res,'')
    uniq = list(set(res))
    return sorted(uniq)


def perm(ss, res, path):
    if ss == '':
        res.append(path)
    else:
        for i in range(len(ss)):
            perm(ss[:i]+ss[i+1:], res, path+ss[i])   # 保存res


print(Permutation('abc'))
