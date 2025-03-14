import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
Max_HIP = []
numbers = []
for _ in range(N):
    number = int(input().strip()) 
    numbers.append(number)

for number in numbers:
    if number == 0:
        if Max_HIP:
            print(-heapq.heappop(Max_HIP))
        else:
            print(0)
    else:
        heapq.heappush(Max_HIP, -number)