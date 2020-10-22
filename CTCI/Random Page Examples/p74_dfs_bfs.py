import pprint
from collections import defaultdict # Why defaultdict? Because it doesn't raise a KeyError, it instead returns a default container that we provide it initially. In our case, it's an empty set.

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False

    def __repr__(self):
        return str(self.value)

class Graph:
    def __init__(self, connections, root=None, directed=False):
        """Graph data structure, undirected by default."""
        self.root = root
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """Add connections (list of tuple pairs) to graph."""
        for node1, node2 in connections:
            self.add(node1, node2)

    def is_empty(self):
        """Return True if graph has no nodes, and False otherwise"""
        return len(self.graph) == 0

    def add(self, node1, node2):
        """Add connection between node1 and node2"""
        if self.is_empty():
            self.root = node1 # By default, take root as the first node of the first tuple given to the connections list
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)

    def get_adjacent_of(self, node):
        """Return all nodes adjacent to a given node"""
        return self.graph[node]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph)) # Casting to dict() just to make output cleaner

def dfs(root):
    if root is None:
        return
    print(root, end=' ')
    root.visited = True
    for node in graph.get_adjacent_of(root):
        if not node.visited:
            dfs(node)

def bfs(root):
    queue = []
    root.visited = True
    queue.append(root)
    while len(queue) > 0:
        dequeued_node = queue.pop(0)
        print(dequeued_node, end=' ')
        for node in graph.get_adjacent_of(dequeued_node):
            if not node.visited:
                node.visited = True
                queue.append(node)


node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

connections = [(node_a, node_b), (node_b, node_c), (node_b, node_d), (node_c, node_d), (node_e, node_f), (node_f, node_c)]
# connections = [(node_a, node_b), (node_a, node_i), (node_i, node_c), (node_i, node_g), (node_c, node_i), (node_c, node_d), (node_c, node_e), (node_c, node_f), (node_e, node_h), (node_f, node_g), (node_g, node_i), (node_g, node_h), (node_h, node_e), (node_h, node_g)]
graph = Graph(connections)
pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(graph.graph)

# dfs(node_a)
print()
bfs(node_a)
