#!/usr/bin/env python

# Graph example used in class
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

# Depth First Search
def dfs(graph, root, visited={}):
    retlist = [root]
    visited[root] = True
    for neighbor in graph[root]:
        if(not visited.has_key(neighbor)):
            retlist += dfs(graph, neighbor, visited)
    return retlist

if __name__ == '__main__':
    print dfs(graph, 'A')
    # ['A', 'B', 'C', 'E', 'D', 'I', 'F', 'G', 'H']