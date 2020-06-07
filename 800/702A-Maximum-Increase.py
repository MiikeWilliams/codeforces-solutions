a, b, m, n = 0, 0, 0, input()
for i in map(int,input().split()):
    m = m + 1 if i > b else 1
    a = max(a, m)
    b = i
print(a)
