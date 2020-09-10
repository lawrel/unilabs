from heapdict import heapdict
import sys
import time

def pop_graph(file):
    graph = {}
    f = open(file, 'r')
    for line in f:
        line = line.split(' ')
        a, b, wgt = int(line[0]), int(line[1]), int(line[2])

        if (a in graph):
            graph[a].append( (b, wgt) )
        else:
            temp = [ (b, wgt) ]
            graph[a] = temp

        if (b not in graph):
            graph[b] = []

    return graph

def gen_dists(graph):
    dists = heapdict()
    for node in graph:
        dists[node] = sys.maxsize

    return dists

def gen_prevs(graph):
    prevs = {}
    for node in graph:
        prevs[node] = 0

    return prevs

def dijkstra(graph, dists, prevs, source):
    shortest = gen_dists(graph)
    dists[source], shortest[source] = 0, 0
    prevs[source] = source

    while (len(dists) > 0):
        reached = dists.popitem()
        node, dist = reached[0], reached[1]
        connected = graph[node]

        if (len(connected) != 0):
            for reach in connected:
                a, b = reach[0], reach[1]
                if (shortest[a] > (dist + b)):
                    dists[a] = (dist + b)
                    shortest[a] = (dist + b)
                    prevs[a] = node

    return shortest

def trail(prevs, node):
    trail = []
    curr = node

    while (prevs[curr] != curr):
        trail.append(curr)
        curr = prevs[curr]

    trail.append(curr)

    return trail[ :: -1]

def run_dijkstra(graph, source):
    dists = gen_dists(graph)
    prevs = gen_prevs(graph)

    shortest = dijkstra(graph, dists, prevs, source)
    for node in shortest:
        print("{}: {}, {}".format(node, shortest[node], trail(prevs, node)))



file = sys.argv[1].strip()
graph = pop_graph(file)

source = input("Input Source Node:")
run_dijkstra(graph, int(source))