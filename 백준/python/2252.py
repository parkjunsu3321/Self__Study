import sys
input = sys.stdin.readline
N, M = map(int, input().split())
come = [[i]for i in range(N)]
outs = [[]for _ in range(N)]
q = []
for _ in range(M):
    a, b = map(int, input().split())
    come[b-1].append(a-1)
    outs[a-1].append(b-1)

come = sorted(come,key=len)

for i in range(N):
    if len(come[i]) == 1:
        print(i+1)
        print()
        for out in outs:
            print(i)
            come[out[i]].remove(i)
