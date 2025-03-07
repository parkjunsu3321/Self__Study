import sys
import math
input = sys.stdin.readline

def IsPrime(data:int):
    if data <= 1:
        return False
    elif data == 2:
        return True
    elif data % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(data)+1),2):
        if data % i == 0:
            return False
    return True

def IsPalindrome(data:int):
    s_data = str(data)
    return s_data == s_data[::-1]

def check(N:int):
    while(True):
        if IsPalindrome(N) and IsPrime(N):
            print(N)
            break
        N+=1

N = int(input())
check(N)