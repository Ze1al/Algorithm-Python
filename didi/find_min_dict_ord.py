# 6
# 3 + 2 + 1 + -4 * -5 + 1

# 输入一个式子，交换相邻的数值使得值保持不变，并且使得字典序最小，字典序定义为 a<b 则a的字典序小于b



def find_min_dict_ord(s):
    for i in range(len(s)):
        if s[i] in ['+','-','*','/']:
            new_s = s
            for j in range(i, 0, -2):
                if int(new_s[j+1])>int(new_s[j-1]):
                    break
                t = new_s[j + 1]
                new_s[j + 1] = new_s[j - 1]
                new_s[j - 1] = t
                if eval(''.join(new_s)) == eval(''.join(s)):
                    s = new_s
                else:
                    break


if __name__ == '__main__':
    n = int(input())
    s = list(input().split(' '))
    find_min_dict_ord(s)
    print(' '.join(s))