import sys
import math

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
stars = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

edges = []
for i in range(n):
    for j in range(i+1, n):
        cost = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edges.append((cost, i, j))

edges.sort()

parent = [i for i in range(n)]
result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(round(result, 2))