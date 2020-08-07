import math
import os
import random
import re
import re
import sys

def timeConversion(s):
    if 'PM' in s:
        t1 = int(s[0:2]) + 12
        if t1 == 24:
            t1 = 12
        return '{0:02d}{1}'.format(t1,s[2:-2])
    else:
        t1 = int(s[0:2])
        if t1 == 12:
            t1 = 0
        return '{0:02d}{1}'.format(t1,s[2:-2])

if __name__ == '__main__':
    s = input().rstrip()
    

    result = timeConversion(s)
    print(result)