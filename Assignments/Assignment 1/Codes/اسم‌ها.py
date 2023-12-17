from collections import Counter

n = int(input())
max = -1
for i in range(n):
    c = Counter(input())
    if len(c) > max:
        max = len(c)

print(max)