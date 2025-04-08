import sys
from collections import defaultdict
input = sys.stdin.readline
time_dict={}
N = int(input())

for _ in range(N):
   in_time, out_time = map(int, input().split())
   time_dict[in_time] = 1
   time_dict[out_time] = -1

times = sorted(time_dict.keys())
current = 0
max_count = 0
max_start = 0
max_end = 0
in_max = False

for time in times:
   current += time_dict[time]
   if current > max_count:
       max_count = current
       max_start = time
       in_max = True
   elif current < max_count and in_max:
       max_end = time
       in_max = False

print(max_count)
print(max_start, max_end)