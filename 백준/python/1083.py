n = int(input())
a = list(map(int, input().split()))
s = int(input())

for i in range(n):
    max_idx = i
    for j in range(i + 1, min(n, i + s + 1)):
        if a[j] > a[max_idx]:
            max_idx = j
    dist = max_idx - i
    if dist > 0:
        s -= dist
        for j in range(max_idx, i, -1):
            a[j], a[j - 1] = a[j - 1], a[j]
    if s == 0:
        break

print(' '.join(map(str, a)))