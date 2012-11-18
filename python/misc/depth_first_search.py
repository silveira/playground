#!/usr/bin/env python

"""
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'A', 'C'],
    'C': ['A', 'D', 'E', 'B'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}
"""

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

def dfs(graph, root, visited={}):
    print root
    visited[root] = True
    for neighbor in graph[root]:
        if(not visited.has_key(neighbor)):
            dfs(graph, neighbor, visited)

dfs(graph, 'A')