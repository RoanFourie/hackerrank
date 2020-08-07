import math
import os
import random
import re
import re
import sys

def birthdayCakeCandles(arr):
    m = max(arr)
    return arr.count(m)


if __name__ == '__main__':
    ar_count = int(input().strip())
    arr = []
    arr = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(arr)
    print(result)