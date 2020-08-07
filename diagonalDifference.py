import math
import os
import random
import re
import re
import sys


def diagonalDifference(arr):
    print(arr)
    i = 0
    res1 = 0
    res2 = 0
    for a in arr:
        res1 += a[i]
        i += 1
    i = n-1
    for a in arr:
        res2 += a[i]
        i -= 1
    return abs(res1 - res2)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

