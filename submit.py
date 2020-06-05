n = int(input())
ax, ay, bx, by = 0, 0, 0, 0
for _ in range(n):
    l = input().split(" ")
    t = int(l[0])
    x = int(l[1])
    y = int(l[2])
    if t == 1:
        ax += x
        ay += y 
    else:
        bx += x
        by += y
print("LIVE" if ax >= ay else "DEAD")
print("LIVE" if bx >= by else "DEAD")
