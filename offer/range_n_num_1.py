# 1~n中1的个数


def NumberOf1Between1AndN_Solution(n):
    count = 0
    i = 1
    while i <= n:
        a = n / i
        b = n % i
        count += (a + 8) / 10 * i + (a % 10 == 1) * (b + 1)
        i *= 10
    return count

print(NumberOf1Between1AndN_Solution(2319))