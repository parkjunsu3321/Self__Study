import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().strip()))
a = 0
for i in range(N):
    a += numbers[i]

print(a)