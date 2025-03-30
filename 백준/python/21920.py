import sys
import math

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
X = int(data[N+1])

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

coprime_sum = 0
coprime_count = 0

for num in A:
    if gcd(X, num) == 1:
        coprime_sum += num
        coprime_count += 1

average = coprime_sum / coprime_count
print(f"{average:.6f}")