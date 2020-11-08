# 32,231
# 23132

def min_num(num):
    fan = str(num)
    if num < int(fan[::-1]):
        return num
    else:
        return int(fan[::-1])

def find_min_num():
    str_input = input()
    arr =[int(i) for i in str_input.split(',')]
    res = []
    for i in arr:
        min = min_num(i)
        res.append(min)
    return ''.join([str(i) for i in res])


if __name__=='__main__':
    print(find_min_num())




