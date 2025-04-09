import sys
input = sys.stdin.readline

N = int(input())
numbers = list(input().split())
num_dict = {}
M = int(input())
checks = list(input().split())
for i in range(N):
    if numbers[i] != None:
        num_dict[numbers[i]] = 1
for check in checks:
    try:
        print(num_dict[check])
    except KeyError:
        print(0)