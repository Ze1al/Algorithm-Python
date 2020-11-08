# 背包问题
# 5
# 10
# 2 2 6 5 4
# 6 3 5 4 6

def bag(n, c, w, v):
    res=[[-1 for j in range(c+1)] for i in range(n+1)]

    for j in range(c+1):
        res[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, c+1):
            res[i][j] = res[i-1][j]
            if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
                res[i][j]=res[i-1][j-w[i-1]]+v[i-1]
    return res[n][c]

if __name__ == '__main__':
    n = int(input())
    c = int(input())
    w = [int(i) for i in input().split(' ')]
    v = [int(i) for i in input().split(' ')]
    print(bag(n,c,w,v))

