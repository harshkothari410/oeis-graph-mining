import sys; import os
sys.path.insert(0, os.path.abspath('..'))

import math
import json
from collections import Counter
from graph import *


# graph.create_adj_matrix('../data/newgraph_dd.json')
# graph = graph.create_graph('../data/graph3.txt')
print graph
from networkx import *

# G=nx.Graph(graph)

f = open('../data/graph3.txt')
G = networkx.read_adjlist(f)
print diameter(G)

