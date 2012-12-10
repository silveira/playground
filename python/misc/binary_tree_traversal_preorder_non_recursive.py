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
	stack = []
	stack.append(root)
	path = []	
	while(len(stack)>0):
		top = stack.pop()
		if (top!=''):
			path.append(top)
			stack.append(graph[top][RIGHT])
			stack.append(graph[top][LEFT])
	return path

print preorder(example_graph, 'A')
