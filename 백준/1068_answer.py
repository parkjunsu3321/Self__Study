def count_leaf_nodes(total_nodes, parents, node_to_delete):
    children = [[] for _ in range(total_nodes)]
    
    root_node = -1
    
    for node, parent in enumerate(parents):
        if parent == -1:
            root_node = node
        else:
            children[parent].append(node)
    
    def dfs(current_node):
        if current_node == node_to_delete:
            return 0
        
        current_children = [child for child in children[current_node] if child != node_to_delete]
        if not current_children:
            return 1
        
        return sum(dfs(child) for child in current_children)
    
    return dfs(root_node)

total_nodes = int(input())
parents = list(map(int, input().split()))
node_to_delete = int(input())

print(count_leaf_nodes(total_nodes, parents, node_to_delete))