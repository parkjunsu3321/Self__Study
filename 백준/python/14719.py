import sys
input = sys.stdin.readline
H, W = map(int, input().split())
block_list = list(map(int, input().split()))

total_water = 0

for i in range(1, W - 1):
    left_max = max(block_list[:i])
    right_max = max(block_list[i+1:])
    
    water_level = min(left_max, right_max)
    if water_level > block_list[i]:
        total_water += water_level - block_list[i]

print(total_water)