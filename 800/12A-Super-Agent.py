M,a=[list(input()) for _ in range(3)],True
for i in range(3):
    for j in range(3):
        if M[i][j] != M[2-i][2-j]:
            a=False
            break
print("YES") if a else print("NO")
