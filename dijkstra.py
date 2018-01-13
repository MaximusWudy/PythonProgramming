#!/usr/bin/python
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set() # set object
        self.edges = defaultdict(list)
        self.distances = {}
        
    def add_nodes(self, value):
        for i in value:
            self.nodes.add(i) # add element into set
        
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node) # dict to neighbour nodes
        self.distances[(from_node, to_node)] = distance # dict for distance
        self.distances[(to_node, from_node)] = distance
    

# -------------------------------------
def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes: 
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
              break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

if __name__ == "__main__":
    g = Graph()
    g.add_nodes([i+1 for i in range(8)])
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 4, 3)
    g.add_edge(2, 5, 7)
    g.add_edge(4, 8, 3)
    g.add_edge(5, 8, 4)
    g.add_edge(3, 6, 3)
    g.add_edge(3, 7, 2)
    g.add_edge(6, 7, 1)
    print "nodes:", g.nodes
    print "edges:", g.edges
    print "distances: ", g.distances
    # ----------
    print "-" * 25
    source_node = 1
    print "Source node:", source_node
    print dijsktra(g, 1) # return with visited and path
