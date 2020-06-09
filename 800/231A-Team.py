c,n=0,int(input())
for _ in range(n):
    if sum(map(int, input().split())) > 1:
        c += 1
print(c)
