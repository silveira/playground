#!/usr/bin/env python

LEFT = 0
RIGHT = 1

example_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['', ''],
    'D': ['G', ''],
    'E': ['', 'F'],
    'F': ['', ''],
    'G': ['', 'H'],
    'H': ['I', ''],
    'I': ['K', ''],
    'K': ['', '']
}

def preorder(graph, root):
    if (root==''):
        return []
    else:
        return [root] + preorder(graph, graph[root][LEFT]) + preorder(graph, graph[root][RIGHT])

def inorder(graph, root):
    if (root==''):
        return []
    else:
        return inorder(graph, graph[root][LEFT]) + [root] + inorder(graph, graph[root][RIGHT])

def postorder(graph, root):
    if (root==''):
        return []
    else:
        return postorder(graph, graph[root][LEFT]) + postorder(graph, graph[root][RIGHT]) + [root]

if __name__ == '__main__':
    print preorder(example_graph, 'A')
    print inorder(example_graph, 'A')
    print postorder(example_graph, 'A')