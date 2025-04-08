import sys
input = sys.stdin.readline
N = int(input())

if N >= 99:
    result = 99
    for num in range(100, N + 1):
        digits = list(map(int, str(num)))
        if digits[1] - digits[0] == digits[2] - digits[1]:
            result += 1
    print(result)
else:
    print(N)