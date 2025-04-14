import sys
input = sys.stdin.readline

ab = list(input().strip())
n = len(ab)
cnt = ab.count("a")
min_b = -1

for i in range(n):
    if i + cnt <= n:
        window = ab[i:i+cnt]
    else:
        window = ab[i:] + ab[:(i + cnt - n)]
    
    b_count = window.count("b")
    if min_b == -1:
        min_b = b_count
    else:    
        min_b = min(min_b, b_count)

print(min_b)
