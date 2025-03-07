class Node:
    number:int
    def __init__(self,number):
        self.number = number
        self.root_node = None
        self.sub_node = []
    
    def setRootNode(self, node):
        self.root_node = node
        node.setSubNode(self)

    def setSubNode(self, node):
        self.sub_node.append(node)

    def getSubNode(self):
        return self.sub_node

def find_subtree_numbers(node):
    numbers = [node.number]
    for sub in node.getSubNode():
        numbers.extend(find_subtree_numbers(sub))
    return numbers

n = int(input())
node_list = list(map(int, input().split()))
n_number = int(input())
nodes = []
num = 0
check = 0
if n <= 50:
    for i in node_list:
        nodes.append(Node(num))
        num+=1
    num = 0
    for i in node_list:
        if i != -1:
            nodes[num].setRootNode(nodes[i])
        num+=1
    delete_numbers = find_subtree_numbers(nodes[n_number])
    result = [x for x in nodes if x not in [nodes[dn] for dn in delete_numbers]]
    for rt in result:
        if rt.getSubNode() == []:
            check+=1
    print(check)