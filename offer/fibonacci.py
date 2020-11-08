
def fibonacci(n):
    res = [1, 1, 2]
    while len(res) <= n:
        res.append(res[-1] + res[-2])
    return res[n]

print(fibonacci(9))