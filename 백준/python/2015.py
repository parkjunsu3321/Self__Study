import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

count = 0
prefix_sum = 0
sum_count = {0: 1}

for num in arr:
    prefix_sum += num
    if prefix_sum - k in sum_count:
        count += sum_count[prefix_sum - k]
    
    if prefix_sum in sum_count:
        sum_count[prefix_sum] += 1
    else:
        sum_count[prefix_sum] = 1

print(count)