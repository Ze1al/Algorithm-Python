# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

def GetUglyNumber_Solution(index):
    if index<=0:
        return 0
    res = [1]
    two_p = 0
    three_p = 0
    five_p = 0
    for i in range(index-1):
        ugly_num = min(res[two_p]*2, res[three_p]*3, res[five_p]*5)
        res.append(ugly_num)
        if ugly_num%2 == 0:
            two_p+=1
        elif ugly_num%3 == 0:
            three_p+=1
        elif ugly_num%5 == 0:
            five_p+=1
    return res[-1]


print(GetUglyNumber_Solution(5))
