import sys
from itertools import combinations

input = sys.stdin.readline
stack = []
indices = []
cnt = 0
results = []
a  = list(input().strip())
for i in range(len(a)):
    if a[i] == '(':
        stack.append(i)
    elif a[i] == ')':
        indices.append((stack.pop(), i))

for i in range(1, len(indices)+1):
    for comb in combinations(indices, i):
        temp = a[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        results.append("".join(temp))

results = sorted(set(results))
for result in results:
    print(result)