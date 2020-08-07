import math
import os
import random
import re
import re
import sys


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    # After thsi section we can run the code and then input the values by typing 6 space 3 Enter then 1 space 3 space 2 space 6 space 1 space 2 enter and the result will follow.
# print(nk, n, k, a)

count = 0
pairs = []
pairs_index = []
index_ignore = []
for i,val1 in enumerate(a): 
    for j,val2 in enumerate(a):
        if i == j:
            continue
        if ((i,j)) in index_ignore:
            continue
        if (val1 + val2)%k == 0:
            count += 1
            pairs.append((val1,val2))
            pairs_index.append((i,j))
            index_ignore.append((j,i))

print(count, pairs, pairs_index)

# Better way using list comprehension:
# n,k = map(int,raw_input().split())
# z = map(int, raw_input().split())

# r = [[i,j] for i in range(n) for j in range(n) if ((z[i] + z[j])%k == 0 and i<j)]
# ptint(len(r))