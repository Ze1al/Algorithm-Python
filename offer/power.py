# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 保证base和exponent不如同时为零

def Power(base, exponent):
    if base == 0.0:
        return 0
    if base==1 or exponent == 0:
        return base
    if exponent == 1:
        return base
    else:
        res = 1
        for i in range(abs(exponent)):
            res *= base
        if exponent<1:
            return 1/res
        else:
            return res

print(Power(2,3))