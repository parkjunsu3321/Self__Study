import sys
input = sys.stdin.readline

def gcd(x,y):
    while y:
        x, y = y, x % y
    return x

N = int(input())
counts = []
for _ in range(N):
    count = list(map(int,input().split()))
    counts.append(count)
gcd_s = []
for cnt in counts:
    gcd_list = []
    for i in range(0,cnt[0]):
        a = i+1
        while(True):
            try:
                gcd_list.append(gcd(cnt[i+1], cnt[a+1]))
                a += 1
            except IndexError:
                break

    gcd_s.append(gcd_list)

for i in range(N):
    print(sum(gcd_s[i]))