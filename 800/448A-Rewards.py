a = (sum(map(int, input().split()))+5-1)//5
b = (sum(map(int, input().split()))+10-1)//10
print("YES") if a + b <= int(input()) else print("NO")
