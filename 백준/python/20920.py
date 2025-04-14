import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = {}
for i in range(N):
    word = str(input().strip())
    try:
        if len(word) >= M:
            words[word] += 1
    except KeyError:
        words[word] = 1

words = dict(sorted(words.items()))
words = dict(sorted(words.items(), key=lambda item: len(item[0]), reverse=True))
words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
for word in words.keys():
    print(word)