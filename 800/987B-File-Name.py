n = int(input())
s = input()
c = 0
for i in range(n - 2):
    if s[i] == s[i+1] == s[i+2] == "x":
        c += 1
print(c)

