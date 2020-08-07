students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
miniv = min(students, key=lambda x: x[1])
filtered = [x for x in students if x[1] != miniv[1]]
minires = min(filtered, key=lambda x: x[1])
# res = [print(x[0]) for x in filtered if x[1] == minires[1]]
res = [x[0] for x in filtered if x[1] == minires[1]]
res.sort()
for ele in res:
    print(ele)

