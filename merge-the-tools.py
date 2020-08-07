string = 'AABCAAADA'
k = 3

i = 0
j = k
a2 = []

while i < len(string):
    a2.append(string[i:j])
    print(i,j)
    i += k
    j += k
for ele in a2:
    cs = list(ele)
    a3 = []
    for c in cs:
        if c not in a3:
            a3.append(c)
    print("".join(a3))

print(a2)

