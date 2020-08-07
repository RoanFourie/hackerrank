grades = [73,67,38,33]

new_grades = []
for i in grades:
    if i == 100:
        new_grades.append(i)
    if i < 38:
        new_grades.append(i)
    else:
        x = int(str(i)[-1])
        y = int(str(i)[-1])
        if x < 5:
            if x >= 3:
                y = 5
        if x > 5:
            if x > 7:
                y = 10
        new_grades.append((int(str(i)[0])*10) + y)
print(new_grades)