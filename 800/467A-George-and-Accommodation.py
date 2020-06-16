r,n=0,int(input())
for _ in range(n):
    p,q=map(int, input().split())
    if p<q-1: r+=1
print(r)
