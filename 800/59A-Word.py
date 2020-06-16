s=input()
u,l=0,0
for n in s:
    if n.upper() == n:
        u+=1
    else:
        l+=1
print(s.upper()) if u > l else print(s.lower())
