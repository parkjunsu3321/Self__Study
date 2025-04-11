from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque(range(1, N + 1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])