#!/usr/bin/env python

# Example used in class
graph = {
    'A': ['B', 'C', 'F'],
    'B': ['C', 'A', 'D', 'E'],
    'C': ['A', 'E', 'B', 'D'],
    'D': ['B', 'E', 'I'],
    'E': ['B', 'C', 'D'],
    'I': ['D'],
    'F': ['A', 'G', 'H'],
    'G': ['H', 'F'],
    'H': ['G', 'F']
}

# Breadth First Search
def bfs(graph, root):
    queue = [root]
    visited = {root:True}
    order = []
    while(len(queue)!=0):
        node = queue.pop(0)
        order.append(node)
        for neighbor in graph[node]:
            if(not visited.has_key(neighbor)):
                queue.append(neighbor)
                visited[neighbor] = True
    return order

if __name__ == '__main__':
	print bfs(graph, 'A')
	# ['A', 'B', 'C', 'F', 'D', 'E', 'G', 'H', 'I']