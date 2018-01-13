Here is a complete version of Python2.7 code regarding the problematic original version. Just paste in in any .py file and run.
Output: The storage objects are pretty clear; dijkstra algorithm returns with first dict of shortest distance from source_node to {target_node: distance length} and second dict of the predecessor of each node, i.e. {2:1} means the predecessor for node 2 is 1 --> we then are able to reverse the process and obtain the path from source node to every other node.

For example, we have {5:2} and {2:1}, which renders that the path from source node 1 to 5 is 1-->2-->5.

And the return output should be :
nodes: set([1, 2, 3, 4, 5, 6, 7, 8])
edges: defaultdict(<type 'list'>, {1: [2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4: [2, 8], 5: [2, 8], 6: [3, 7], 7: [3, 6], 8: [4, 5]})
distances: {(1, 2): 4, (7, 3): 2, (1, 3): 1, (6, 7): 1, (4, 8): 3, (8, 5): 4, (7, 6): 1, (3, 1): 1, (2, 1): 4, (6, 3): 3, (3, 6): 3, (3, 7): 2, (4, 2): 3, (2, 5): 7, (5, 2): 7, (2, 4): 3, (5, 8): 4, (8, 4): 3}

original source: https://gist.github.com/econchick/4666413
