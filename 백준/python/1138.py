import sys
input = sys.stdin.readline

N = int(input())
tall_left = list(map(int, input().split()))

result = [0] * N

for i in range(N):
    count = tall_left[i]
    
    for j in range(N):
        if result[j] == 0:
            if count == 0:
                result[j] = i + 1
                break
            count -= 1
print(' '.join(map(str, result)))