N, L = map(int, input().split())
if N <= 1000000000 and L>=2 and L<=100:
    while True:
        sum = 0
        if L > 100:
            print(-1)
            break
        for i in range(1, L):
            sum += i
        a = (N-sum)/L
        if a.is_integer():
            if a < 0:
                print(-1)
                break
            else:
                for i in range(0, L):
                    print(int(a+i))
                break
        else:
            L+=1
else:
    print(-1)