string_lst = list(input())
lst = []

for i in range(len(string_lst)):
    if string_lst[i] == "=":
        lst.pop()
    else:
        lst.append(string_lst[i])

print(''.join(lst))