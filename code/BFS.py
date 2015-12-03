'''
BFS
'''
import sys
from Digraph import *
from collections import deque
class BFS:

    INFINITY = sys.maxint

    def __init__(self, graph, source):
        V = graph.numOfVertices()
        self.source = source
        self.marked = [False for i in range(V)]
        self.distTo = [BFS.INFINITY for i in range(V)]
        self.edgeTo = [0 for i in range(V)]
        self.bfs(graph, source)

    def bfs(self, graph, source):
        queue = deque()
        queue.append(source)
        self.marked[source] = True
        self.distTo[source] = 0
        while queue:
            curr = queue.popleft()
            for w in graph.adjacent(curr):
                if not self.marked[w]:
                    self.edgeTo[w] = curr;
                    self.distTo[w] = self.distTo[curr] + 1
                    self.marked[w] = True
                    queue.append(w)

    def hasPathTo(self, v):
        return self.marked[v]

    def distanceTo(self, v):
        return self.distTo[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = []
        x = v
        while self.distTo[x] != 0:
            path.append(x)
            x = self.edgeTo[x]
        path.append(x)
        path.reverse()
        return path

if __name__ == "__main__":
    graph = Digraph(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    source = 1
    bfs = BFS(graph, source)
    for i in range(graph.numOfVertices()):
        if bfs.hasPathTo(i):
            print "%d to %d (%d)" % (source, i, bfs.distanceTo(i))
            for x in bfs.pathTo(i):
                if x == source: print x,
                else: print "-> " + str(x),
            print "\n"
        else:
            print "%d to %d (-) : not connected\n" % (source, i)




