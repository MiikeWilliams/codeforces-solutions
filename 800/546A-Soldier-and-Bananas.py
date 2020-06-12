k,n,w=list(map(int, input().split()))
c=0
for i in range(1, w+1):
    c=k*i+c
print(abs(c-n)) if c > n else print(0)
