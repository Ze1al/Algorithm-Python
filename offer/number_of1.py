 # 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
 # 二进制用32位表示，负数的二进制表示方法为补码，补码是原码的基础上加一


def NumberOf1(n):
    count = 0
    for i in range(32):
        count += (n >> i) & 1   # 每一位都移动一下，判断最后一位是不是1，是1就加1
    return count

print(NumberOf1(5))
