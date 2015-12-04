import sys
import json
f = open('connected.txt','r')
f1 = open('graph3.txt','r')


s=f.read();
# s1=f1.read();
s = s.replace('"','')
s = s.replace('[','')
s = s.replace(']','')
s = s.replace(',','')

s = s.split()
def create_graph():
	graph = {}
	lines = f1.read().splitlines()

	count = 0
	for line in lines:
		l = line.split(' ')
		# graph[l[0]] = set(l[1:])
		graph[l[0]] = l[2:]
		# if count == 9:
		# 	return graph

		# count = count  + 1
	return graph

# def binary_search(seq, t):
#     min = 0
#     max = len(seq) - 1
#     while True:
#         if max < min:
#             return -1
#         m = (min + max) // 2
#         if seq[m] < t:
#             min = m + 1
#         elif seq[m] > t:
#             max = m - 1
#         else:
#             return m


#graph = create_graph()
k=0
data = {}
temp=[]
# x=0


ng = open('newgraph_dd50.json')
graph = json.loads(ng.read())


count = 0
for x in s:
	#for y in range(0,len(s1)-1):
	#	if x == s1[y][0]:
	#		temp.append(s1[y][:])
	#		k=k+1
	# print x
	if x in graph.keys():
		data[x] = graph[x]

	#if count == 50:
	#	break

	count = count + 1
	print count
	# if x not 0

print count
g = open('connected_list.json', 'w')
json = json.dumps(data, indent=4)
g.write(json)
g.close()
