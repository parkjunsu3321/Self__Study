import sys
input = sys.stdin.readline
str_list = list(input().rstrip())
result_dict = {}

for string in str_list:
    try:
        result_dict[string.upper()] += 1
    except KeyError:
        result_dict[string.upper()] = 1

v = max(result_dict.values())

result = [k for k, i in result_dict.items() if i == v]

if len(result) == 1:
    print(result[0])
else:
    print("?")