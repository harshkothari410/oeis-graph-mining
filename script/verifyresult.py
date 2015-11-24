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

print calculate_edge(s_graph['94638'], s_graph['984'])
