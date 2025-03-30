import sys
input = sys.stdin.readline
words = []
l = 0
for i in range(5):
    word = list(input().strip())
    words.append(word)

for word in words:
    if l <= len(word):
        l = len(word)

output = ''
for j in range(l):
    for i in range(5):
        try:
            output += words[i][j]
        except IndexError:
            continue
print(output)