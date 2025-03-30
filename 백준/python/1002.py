n = int(input())
a = []
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d =((x2 - x1)**2 +(y2 - y1)**2)**0.5
    if x1==x2 and y1==y2:
        if r1 == r2:
            a.append(-1)
        else:
            a.append(0)
    else:
        if d > r1+r2:
            a.append(0)
        elif d == r1+r2:
            a.append(1)
        elif abs(r1-r2) < d < r1+r2:
            a.append(2)
        elif d == abs(r1-r2):
            a.append(1)
        else:
            a.append(0)
for i in a:
    print(i)