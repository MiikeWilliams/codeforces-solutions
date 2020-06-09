for _ in range(int(input())):
    s = input(); l = len(s)-2
    print([s, s[0]+str(l)+s[-1][l>8]])
