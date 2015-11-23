f = open('graph3.txt','r')

def create_graph():
	graph = {}
	lines = f.read().splitlines()

	count = 0
	for line in lines:
		l = line.split(' ')
		# graph[l[0]] = set(l[1:])
		graph[l[0]] = set(l[1:])
		# if count == 9:
		# 	return graph

		# count = count  + 1
	return graph

def bfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop(0)
		print path
		if path[-1] == '0':
			continue
		for next in graph[vertex] - set(path):
			if next == goal:
				# yield path + [next]
				return path + [next]
			else:
				stack.append((next, path + [next]))
	return 'No Path'


graph = create_graph()

# print graph
print "Enter the First Sequence No : "
a = raw_input()
print "Enter the second Sequence No : "
b = raw_input()
print "Path Between : " + a + " and " + b
print (bfs_paths(graph, a, b))