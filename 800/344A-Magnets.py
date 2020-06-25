couter,n,prev=1,int(input()),input()
for _ in range(1, n):
    current=input()
    if prev != current:
        couter+=1
    prev=current
print(couter)

