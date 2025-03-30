def push(q:list, data):
    q.append(data)

def pop(q:list):
    if q == []:
        print(-1)
    else:
        print(q[0])
        del q[0]

def size(q:list):
    print(len(q))

def empty(q:list):
    if len(q) == 0:
        print(1)
    else:
        print(0)

def back(q):
    if q == []:
        print(-1)
    else:
        print(q[-1])

def front(q):
    if q == []:
        print(-1)
    else:
        print(q[0])

N = int(input())
q = []
commands = []
for _ in range(N):
    command = input().split()
    commands.append(command)
for i in range(N):
    if commands[i][0] == "push":
        push(q, commands[i][1])
    elif commands[i][0] == "pop":
        pop(q)
    elif commands[i][0] == "size":
        size(q)
    elif commands[i][0] == "empty":
        empty(q)
    elif commands[i][0] == "back":
        back(q)
    elif commands[i][0] == "front":
        front(q)