from Digraph import *
from BFS import *
from OEIS import *
import sys

if __name__ == '__main__':
    oeis = OEIS(sys.argv[1], sys.argv[2])
    graph = oeis.graph
    source = int(sys.argv[3]) - 1
    bfs = BFS(graph, source)
    freq = {}
    for i in range(graph.numOfVertices()):
        if bfs.hasPathTo(i):
            dist = bfs.distanceTo(i)
            freq[dist] = freq.get(dist, 0) + 1
    total = 0
    product = 0
    for key, value in freq.items():
        total += value
        product += key * value
        print key, value
    print "%d of %d is reachable" %(total, graph.numOfVertices())
    print "average distance is %.2f"%(product / float(total))
    while True:
        sink = int(raw_input()) - 1
        if bfs.hasPathTo(sink):
            print "%d %d (%d)" % (source, sink, bfs.distanceTo(sink))
            for v in bfs.pathTo(sink):
                print "%d %s" % (v + 1, oeis.getTitle(v))
        else:
            print "Not connected"
