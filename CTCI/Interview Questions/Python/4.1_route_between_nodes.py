# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

from collections import defaultdict
import pprint

class Node:
    def __init__(self, val):
        self.val = val
        self.visited = False

    def __repr__(self):
        return str(self.val)

class Graph:
    """Undirected graph class."""
    def __init__(self, connections):
        self.root = None
        self.graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            if self.root is None:
                self.root = node1
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)

    def get_adjacent_of(self, node):
        return self.graph[node]

    def get_nearest_unvisited_neighbour(self, node):
        """Returns the neighbour that is alphabetically the most closest to the given node"""
        if len(self.graph[node]) == 0:
            return None
        nearest = None
        for node in self.graph[node]:
            if not node.visited:
                if nearest is None:
                    nearest = node
                else:
                    if node.val < nearest.val:
                        nearest = node
        return nearest

    # Solution 0
    # Well, this is the easy way out. But this is probably not what the question was asking me to do.
    def is_connected(self, node1, node2):
        return node1 in self.graph[node2]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph)) # Casting to dict() just to make output cleaner

# Solution 1
# Do BFS starting at node 1. If node2 found during traversal, that means a route exists so return True
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def is_connected_bfs(node1, node2):
    if node1 == node2:
        return True
    queue = [node1]
    node1.visited = True
    while len(queue) > 0:
        current = queue.pop(0)
        if current == node2: # If node2 is found at any point during BFS, return True
            return True
        for node in graph.get_adjacent_of(current):
            if not node.visited:
                node.visited = True
                queue.append(node)
    return False

# Solution 2
# Iterative DFS. If node2 found anywhere during traversal, return True
# I did an iterative version because I needed to return a boolean, and I felt recursion wasn't a good idea due to that.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def is_connected_dfs(node1, node2):
    if node1 == node2:
        return True
    stack = [node1]
    node1.visited = True
    while len(stack) > 0:
        current = stack[-1]
        neighbour = graph.get_nearest_unvisited_neighbour(current)
        if neighbour is None:
            stack.pop()
        else:
            stack.append(neighbour)
            neighbour.visited = True
            if neighbour == node2:
                return True
    return False

node_a = Node('A'); node_b = Node('B'); node_c = Node('C'); node_d = Node('D'); node_e = Node('E'); node_f = Node('F')
connections = [(node_a, node_b), (node_b, node_c), (node_b, node_d), (node_c, node_d), (node_e, node_f), (node_f, node_c)]
graph = Graph(connections)
pprint.PrettyPrinter().pprint(graph.graph)

# Solution 1
print('Path from {} to {}? : {}'.format(node_a.val, node_b.val, graph.is_connected(node_a, node_b)))
print('Path from {} to {}? : {}'.format(node_a.val, node_f.val, graph.is_connected(node_a, node_f)))

# Solution 2
print('Path from {} to {}? : {}'.format(node_a.val, node_b.val, is_connected_bfs(node_a, node_b)))
print('Path from {} to {}? : {}'.format(node_a.val, node_f.val, is_connected_bfs(node_a, node_f)))

# Doing this again because all the nodes have been set to visited by BFS
node_a = Node('A'); node_b = Node('B'); node_c = Node('C'); node_d = Node('D'); node_e = Node('E'); node_f = Node('F')
connections = [(node_a, node_b), (node_b, node_c), (node_b, node_d), (node_c, node_d), (node_e, node_f), (node_f, node_c)]
graph = Graph(connections)

# Solution 3
print('Path from {} to {}? : {}'.format(node_a.val, node_b.val, is_connected_dfs(node_a, node_b)))
print('Path from {} to {}? : {}'.format(node_a.val, node_f.val, is_connected_dfs(node_a, node_f)))
