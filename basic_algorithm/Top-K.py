# 海量数据Top k


def partition(seq):
    qviot, seq = seq[0], seq[1:]                 # 选取并移除主元
    right = [x for x in seq if x <= qviot]      # 值较小的
    left = [x for x in seq if x > qviot]
    return right, qviot, left

def select(seq, k):
    right, qviot, left = partition(seq)
    m = len(right)
    if m == k:
        return right
    if m < k:
        right.append(qviot)
        return right+select(left, k-m-1)
    return select(right, k)


if __name__ == "__main__":
    sel = [8,3,4,5,1,5,23,5,1,3,53,645,314,632,65,76,2,46,575,1,5]
    print(select(sel, 5))
