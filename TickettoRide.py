# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_nodes(self, value):
        for i in value:
            self.nodes.add(i)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijkstra(graph, initial):
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


n_node = int(raw_input().strip())
g = Graph()
g.add_nodes([i + 1 for i in range(n_node)])
for i in range(n_node - 1):
    start, end, cost = map(int, raw_input().strip().split(" "))
    g.add_edge(start, end, cost)


# know from setting that network is tree: node = arc + 1

def createPath(path, source):
    dict_path = defaultdict(list)
    for node in path:
        dict_path[node].append(node)
        while dict_path[node][-1] != source:
            dict_path[node].append(path[dict_path[node][-1]])
    for node in dict_path:
        dict_path[node].reverse()
    return dict_path


result_dict = defaultdict(list)
for node in range(1, n_node + 1):
    shortest_d, path = dijkstra(g, node)
    result_dict[node].append(shortest_d)
    dict_path = createPath(path, node)
    result_dict[node].append(dict_path)
    # now we have result_dict with all info

ticket_n = int(raw_input().strip())
ticket_dict = {}
for i in range(ticket_n):
    depart, dest, price = map(int, raw_input().strip().split(" "))
    if (depart, dest) in ticket_dict:
        if ticket_dict[(depart, dest)] != price:
            ticket_dict[(depart, dest)] += price
    else:
        ticket_dict[(depart, dest)] = price

max_profit = 0
for start in range(1, n_node):
    for end in range(start + 1, n_node + 1):
        path_set = set(result_dict[start][1][end])
        profit = sum([ticket_dict[key] for key in ticket_dict if set(key).issubset(path_set)]) - result_dict[start][0][
            end]
        print "Pair: ", (start, end)
        print "Distance:", result_dict[start][0][end]
        print "List: ", [ticket_dict[key] for key in ticket_dict if set(key).issubset(path_set)]
        print "Profit:", profit

        # profit  = Ticket Price - Build Cost
        if profit > max_profit:
            max_profit = profit

print max_profit
