from Digraph import *
from BFS import *
import sys
class OEIS:

    def __init__(self, edges, title):
        self.id2name = dict()
        self.readTitle(title)
        self.graph = Digraph(len(self.id2name))
        self.readEdge(edges)
        #sanity check
        print "# of vertices ", self.graph.numOfVertices()
        print "# of edges ", self.graph.numOfEdges()

    def readTitle(self, title):
        f = open(title, 'r')
        lines = f.readlines()
        for line in lines:
            tokens = line.split(' ', 1)
            id = int(tokens[0]) - 1
            definition = tokens[1]
            self.id2name[id] = definition

    def readEdge(self, edges):
        f = open(edges, 'r')
        lines = f.readlines()
        total = 0
        for line in lines:
            tokens = line.split()
            start = int(tokens[0]) - 1
            count = int(tokens[1])
            if count != len(tokens) - 2:
                raise Exception("not match")
            total += count
            if count == 0: continue
            for end in tokens[2:]:
                end = int(end) - 1
                if end >= len(self.id2name): continue
                self.graph.addEdge(start, end)

    def getTitle(self, v):
        return self.id2name[v]

if __name__ == "__main__":
    oeis = OEIS(sys.argv[1], sys.argv[2])













