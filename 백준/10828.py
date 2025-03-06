def push(stack:list, data):
    stack.append(data)

def pop(stack:list):
    if stack == []:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]

def size(stack:list):
    print(len(stack))

def empty(stack:list):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top(stack):
    if stack == []:
        print(-1)
    else:
        print(stack[-1])

N = int(input())
stack = []
commands = []
for _ in range(N):
    command = input().split()
    commands.append(command)
for i in range(N):
    if commands[i][0] == "push":
        push(stack,commands[i][1])
    elif commands[i][0] == "pop":
        pop(stack)
    elif commands[i][0] == "size":
        size(stack)
    elif commands[i][0] == "empty":
        empty(stack)
    elif commands[i][0] == "top":
        top(stack)