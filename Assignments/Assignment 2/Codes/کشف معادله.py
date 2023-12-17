import math

def f1(x):
    return(x - math.floor(x))

def f2(x):
    return(x**2 + x)

def f3(x):
    return(abs(-(x**3) + 1) + x**3)

n = int(input())

f_check = [True, True, True]
for i in range(n):
    x, y = map(float, input().split())
    f_check = [
        f_check[0] and round(abs(f1(x) - y), 10) <= 0.2, 
        f_check[1] and round(abs(f2(x) - y), 10) <= 0.2, 
        f_check[2] and round(abs(f3(x) - y), 10) <= 0.2
    ]

print(f_check.index(True) + 1 if True in f_check else 'No ones')