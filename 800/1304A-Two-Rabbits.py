for _ in range(int(input())):
    x,y,a,b=map(int, input().split())
    print((y-x)//(a+b)) if (y-x)%(a+b) == 0 else print(-1)
