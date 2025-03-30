import sys
sys.setrecursionlimit(10**7)
n = int(input())
node_list = list(map(int, input().split()))
n_number = int(input())
rm_list=[]
def checkChild(tree,num):
    temp=[]
    for child in tree[num]:
        if tree[child] == []:
            temp.append(child)
        else:
            temp.extend(checkChild(tree,child))
    return temp

if n <= 50:
    tree = [[] for _ in range(n)]
    root = -1
    for child, parent in enumerate(node_list):
        if parent != -1:
            tree[parent].append(child)
    numbers = [n_number]
    numbers.extend(checkChild(tree,n_number))
    for num in numbers:
        rm_list.append(tree[num])
    
    for rm in rm_list:
        tree.remove(rm)

    check = 0
    for node in tree:
        if node == []:
            check+=1
    print(check)