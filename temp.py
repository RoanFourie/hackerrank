import math
import os
import random
import re
import re
import sys


n = float(input().rstrip())
lst = [int(x) for x in input().rstrip().split()]
print(round(len([x for x in lst if x > 0])/n, 6))
print(round(len([x for x in lst if x < 0])/n, 6))
print(round(len([x for x in lst if x == 0])/n, 6))

