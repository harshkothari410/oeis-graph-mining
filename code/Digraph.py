'''
Directed graph
'''
class Digraph:

    def __init__(self, V):
        self.V = V #number of vertices
        self.E = 0 #number of edges
        self.adj = [[] for i in range(V)] #adjacent list

    def addEdge(self, v, w):
        self.checkVertex(v);
        self.checkVertex(w);
        self.adj[v].append(w)
        self.E += 1

    def adjacent(self, v):
        self.checkVertex(v);
        return self.adj[v]

    def checkVertex(self, v):
        if v < 0 or v >= self.V:
            raise Exception("index out of bound")

    def numOfVertices(self):
        return self.V

    def numOfEdges(self):
        return self.E


#unit test
if __name__ == "__main__":
    graph = Digraph(4)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    print graph.adj
    print graph.adjacent(0)
    print "# of edges", graph.numOfEdges();
    print "# of vertices", graph.numOfVertices();
