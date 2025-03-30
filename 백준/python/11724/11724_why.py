import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(connect_list:list, visit:list, i:int):
    visit[i] = True
    for j in connect_list[i]:
        if not visit[j]:
            DFS(connect_list, visit, j)
    
V, E = map(int, input().split())
connect_list = [[] for _ in range(V)]
for i in range(E):
    now, next = map(int, input().split())
    connect_list[now-1].append(next-1)
    connect_list[next-1].append(now-1)

visit = [False for _ in range(V)]
count = 0
for i in range(V):
    if not visit[i]:
        DFS(connect_list, visit, i)
        count += 1

print(count)