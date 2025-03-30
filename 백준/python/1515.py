import sys
input = sys.stdin.readline

s = input().strip()
idx = 0
num = 1

while idx < len(s):
    num_str = str(num)
    for digit in num_str:
        if idx < len(s) and digit == s[idx]:
            idx += 1
    num += 1

print(num - 1)