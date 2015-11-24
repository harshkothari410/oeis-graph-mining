import requests
import json
import sys

# class NoIndent(object):
#     def __init__(self, value):
#         self.value = value

# def default(o, encoder=json.JSONEncoder()):
#     if isinstance(o, NoIndent):
#         return json.dumps(o.value)
#     return encoder.default(o)


g = open('../data/catalans.txt')
h = open('../data/sequence.txt')
f = open('../data/graph3.txt','r')


def seq_graph():
	s = h.read()
	return json.loads(s)

def create_graph():
	graph = {}
	lines = f.read().splitlines()

	count = 0
	for line in lines:
		l = line.split(' ')
		# graph[l[0]] = set(l[1:])
		graph[l[0]] = set(l[2:])
		# if count == 9:
		# 	return graph

		# count = count  + 1
	return graph

def calculate_edge(seq1, seq2):
	weight = 0
	for x in range(10):
		weight = weight + abs(seq1[x] - seq2[x])
	return weight

def calculate_edge1(seq1, seq2):
	weight = 1
	for x in range(10):
		if abs(seq1[x] - seq2[x]):
			weight = weight + 1
		else:
			continue
	return weight

graph = create_graph()
s_graph = seq_graph()
lines = g.read().splitlines()
dirty = []
data = {}
lines = lines[1:]
main = 0
for line in lines:

	try:
		seq1_name = line.split(' ')[0]
		main = seq1_name
		seq1 = s_graph[seq1_name]
		seq2_list = graph[seq1_name]

		temp = {}
		for seq2_name in seq2_list:
			main = seq2_name
			seq2 = s_graph[seq2_name]
			weight = calculate_edge1(seq1, seq2)
			 # print seq1_name + '  ' + seq2_name + '  ' + str(weight)
			temp[seq2_name] = weight
	except:
		dirty.append(main)

	data[seq1_name] = temp

newgraph = open('../data/newgraph.json', 'w')
json = json.dumps(data, sort_keys=True, indent=4)
newgraph.write(json)
newgraph.close()
print dirty
