import math
import os
import random
import re
import re
import sys


def plusMinus(arr):
    pos = 0
    o = 0
    neg = 0
    for v in arr:
        if v > 0:
            pos += 1
        elif v < 0:
            neg += 1
        else:
            o += 1
    print(round(pos/n,6))
    print(round(neg/n,6))
    print(round(o/n,6))


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)



# A better way:
# n = float(input().rstrip())
# lst = [int(x) for x in input().rstrip().split()]
# print(round(len([x for x in lst if x > 0])/n, 6))
# print(round(len([x for x in lst if x < 0])/n, 6))
# print(round(len([x for x in lst if x == 0])/n, 6))