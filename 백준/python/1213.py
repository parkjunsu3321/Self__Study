import sys
input = sys.stdin.readline

def init_palindrome_dict(world:str):
    palindrome_dict = {}
    for i in range(len(world)):
        if world[i] not in palindrome_dict.keys():
            palindrome_dict[world[i]] = 1
        else:
            palindrome_dict[world[i]] += 1
    return palindrome_dict

def can_be_palindrome(data:dict):
    count = 0
    for v, i in data.items():
        if i % 2 != 0:
            if count == 1:
                return False
            else:
                count += 1
    return True

def make_palindrome(data:dict):
    palindrome = ""
    mid_world = ""
    for i in data.keys():
        if data[i] % 2 != 0:
            mid_world = i
        num = int(data[i] / 2)
        for j in range(num):
            palindrome += i
    reverse_data = palindrome[::-1]
    palindrome += mid_world
    palindrome += reverse_data
    print(palindrome)

world = input().strip()
data = init_palindrome_dict(world)
sorted_data = dict(sorted(data.items()))
if can_be_palindrome(data):
    make_palindrome(sorted_data)
else:
    print("I'm Sorry Hansoo")