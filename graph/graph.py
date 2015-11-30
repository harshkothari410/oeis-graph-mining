"""
File for creating graph from text file
"""

def create_graph(filename):
	f = open(filename,'r')
	graph = {}
	lines = f.read().splitlines()

	count = 0
	for line in lines:
		l = line.split(' ')
		graph[l[0]] = l[1:]

	f.close()
	return graph

def count_all_nodes(graph):
	return len(graph)

def count_node(graph, id):
	return len(graph[id])