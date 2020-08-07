arr = list(map(int, input().rstrip().split()))
mini = []
maxi = []
mini.extend(arr)
mini.remove(min(arr))

maxi.extend(arr)
maxi.remove(max(arr))

print(sum(maxi), sum(mini))