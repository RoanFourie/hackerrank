string = "I am an Indian, by birth"
sub_string = "birth"
i = 0
count = 0
while (i < len(string) - len(sub_string)) and (i >=0):
    i = string.find(sub_string,i)
    if i == -1:
        break
    i += 1
    if i > 0:
        count += 1

print(count)
