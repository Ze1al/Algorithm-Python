
import sys

def is_ture_or_false_of_test(arr):
    n = len(arr)
    for i in range(1, n+1, 2):
        print(whois_big(arr[i], arr[i+1]))


def whois_big(A, B):
    A_arr = A.split('.')
    B_arr = B.split('.')
    n = len(A_arr)
    for i in range(0, n, -1):
        if A_arr[i] > B_arr[i]:
            return False
    return True


if __name__ == "__main__":
    strList = []
    for line in sys.stdin:
        tempStr = line.split()
        strList.extend(tempStr)
    is_ture_or_false_of_test(strList)
