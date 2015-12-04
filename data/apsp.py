import networkx as nx
import json
fh=open("connected_list.json", 'r')

# fh=open(".json", 'r')
#G=nx.read_adjlist(fh)
sd=json.loads(fh.read())
#G=nx.path_graph(5)
# path=nx.single_source_shortest_path(G,0)
# path[4]

# G = nx.read(fh)
# data = json_graph.adjacency_data(G)
# H = json_graph.adjacency_graph(data)

G = nx.Graph(sd)

v1 = '107132'
# path=nx.single_source_shortest_path(G,v1)
path = nx.all_pairs_shortest_path(G)

max = 0
node = '0'
for k,v in path.items():
	if max < len(v):
		max = len(v)
		node = k
print len(list(path.keys()))

fname = 'apsp.json'
f = open(fname, 'w')
data = json.dumps(path, indent=4)
f.write(data)
f.close()