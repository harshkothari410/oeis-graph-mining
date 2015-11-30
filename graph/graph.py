"""
File for creating graph from text file
"""
import json

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

def create_adj_matrix(filename):
	with open(filename) as data_file:    
		data = json.load(data_file)
	# data = json.loads(f)
	graph = {}
	# lines = f.read().splitlines()

	count = 0
	# for line in lines:
	# 	l = line.split(' ')
	# 	graph[l[0]] = l[1:]

	# for k, v in data.items():
	k = '1'
	v = data[k]

	d = [2]*len(data)
	for k1, v1 in v.items():
		d[int(k1)] = v1

	graph['1'] = d

	# f.close()

	f = open('../data/newgraph_adj_dd.json', 'w')
	j = json.dumps(graph)
	f.write(j)

	return graph