# 钜形覆盖问题

def rectCover(number):
    a = 1
    b = 1
    for i in range(number):
        a, b = b, a+b
    return a

rectCover(5)