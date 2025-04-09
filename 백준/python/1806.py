import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

def find_minimum_length():
    left = 0
    total = 0
    min_length = N+1
    
    for right in range(N):
        total += numbers[right]
        
        while total >= S and left <= right:
            min_length = min(min_length, right - left + 1)
            total -= numbers[left]
            left += 1
    
    return min_length if min_length <= N else 0

result = find_minimum_length()
print(result)