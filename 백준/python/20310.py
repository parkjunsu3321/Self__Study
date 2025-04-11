import sys
input = sys.stdin.readline

S = input().strip()
zero = S.count('0') // 2
one = S.count('1') // 2

result = []
for ch in S:
    if ch == '1' and one > 0:
        one -= 1
        continue
    result.append(ch)

final = []
for ch in reversed(result):
    if ch == '0' and zero > 0:
        zero -= 1
        continue
    final.append(ch)

print(''.join(reversed(final)))