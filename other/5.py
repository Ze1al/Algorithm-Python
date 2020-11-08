# 计算最少要用几次按键
# 输入：AaAAAA
# 输出8

# 1. 边界条件： n<=0, return 0
# 2. 判断第一个字符是不是大写，大写 res+1
# 3. 连着2个字母以上都是大写或者小写 就 res=长度+2（用const方法）
# 4. 连着2个字母不一样就用 res += 3

def count_keyboard():
    n = int(input())
    a = input()
    count = len(a)
    if a[0].isupper():
        count += 1
    for i in range(1, n):
        if a[i].islower() and a[i - 1].isupper():
            count += 1
        elif a[i].isupper() and a[i - 1].islower():
            count += 1
    print(count-1)

count_keyboard()