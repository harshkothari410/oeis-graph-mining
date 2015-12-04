import networkx as nx
import json
# fh=open("connected_list.json", 'r')

fh=open("newgraph_dd50.json", 'r')
#G=nx.read_adjlist(fh)
sd=json.loads(fh.read())
#G=nx.path_graph(5)
# path=nx.single_source_shortest_path(G,0)
# path[4]

# G = nx.read(fh)
# data = json_graph.adjacency_data(G)
# H = json_graph.adjacency_graph(data)

G = nx.Graph(sd)

v1 = '46'
path=nx.single_source_dijkstra_path(G,v1, weight='weight')


max = 0
node = '0'
for k,v in path.items():
	if max < len(v):
		max = len(v)
		node = k
print len(list(path.keys()))
print max, node

fname = 'ssdij' + v1 + '.json'
f = open(fname, 'w')
data = json.dumps(path, indent=4)
f.write(data)
f.close()