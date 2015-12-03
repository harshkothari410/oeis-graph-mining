import sys
f = open('../data/graph3.txt','r')

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

graph = create_graph()
count = 0
def dfs(start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

count = 0

allnodes = list(graph.keys())
allnodes.reverse()
visitednodes = []
cc = []

# # current = allnodes.pop()
# while len(allnodes) != 0:
# 	print '==============='
# 	count = count + 1

	
# 	current = allnodes.pop()
# 	print current
# 	if current in visitednodes:
# 		continue
# 	else:

# 		s1 = dfs(current)
		
# 		print " Length of current dfs run : " + str(len(s1))	

# 		s1 = list(s1)	
# 		visitednodes = visitednodes + s1
# 		c = 0

# 		# print s1
# 		cc.append(s1)
# 		print " Connected Comp count :  " +  str(len(cc))
# 		print " Length of visitednodes :  " + str(len(visitednodes))
# 		# print len(list(graph.keys()))

# 		# print cc

# 	# if count == 2:
# 	# 	break

# print s1

# s1 = list(dfs('1'))


# print len(visitednodes)
# print len(allnodes)
# print len(s1)

# import json
# g = open('../data/connected.txt', 'w')


# jon  = json.dumps(s1)
# g.write(jon)
# g.close()

print list(dfs_paths(graph,'46','127892'))