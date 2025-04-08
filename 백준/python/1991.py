import sys
input = sys.stdin.readline

def Preorder_Traversal(tree, node):
    result = node
    if tree[node][0] != " ":
        result += Preorder_Traversal(tree, tree[node][0])
    if tree[node][1] != " ":
        result += Preorder_Traversal(tree, tree[node][1])
    return result

def Inorder_Traversal(tree, node):
    result = ""
    if tree[node][0] != " ":
        result += Inorder_Traversal(tree, tree[node][0])
    result += node
    if tree[node][1] != " ":
        result += Inorder_Traversal(tree, tree[node][1])
    return result

def Postorder_Traversal(tree, node):
    result = ""
    if tree[node][0] != " ":
        result += Postorder_Traversal(tree, tree[node][0])
    if tree[node][1] != " ":
        result += Postorder_Traversal(tree, tree[node][1])
    result += node
    return result

tree = {}
N = int(input())
for _ in range(N):
    a, b, c = input().split()
    tree[a] = [b if b != '.' else " ", c if c != '.' else " "]

print(Preorder_Traversal(tree, "A"))
print(Inorder_Traversal(tree, "A"))
print(Postorder_Traversal(tree, "A"))