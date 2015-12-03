from Digraph import *
from BFS import *
from OEIS import *
import sys

def getNext(graph, vertices):
    bfsList = [BFS(graph, vertex) for vertex in vertices]
    V = graph.numOfVertices()
    maxDist = 0
    res = -1
    for i in range(V):
        dist = 0
        isConnected = True
        for bfs in bfsList:
            if not bfs.hasPathTo(i): isConnected = False
            dist += bfs.distanceTo(i)
        if isConnected and dist > maxDist:
            if i not in vertices:
                maxDist = dist
                res = i
    print "%d with distance %d" %(res, maxDist)
    distList = [bfs.distanceTo(res) for bfs in bfsList]
    print distList
    return res

if __name__ == '__main__':
    oeis = OEIS(sys.argv[1], sys.argv[2])
    graph = oeis.graph
    vertices = [127892 - 1, 181085 - 1]
    for i in range(14 - 2):
        nextVertex = getNext(graph, vertices)
        vertices.append(nextVertex)
        print vertices
                
