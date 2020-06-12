n=int(input())
t,m=0,-1
for _  in range(n):
    a,b=map(int,input().split())
    t = t + (b-a)
    m = max(t, m)
print(m)
