def h(x):
    x = abs(x)
    res = 0
    while x:
        res += 1
        x //= 10
    return res

num = int(input())

print(f(num))