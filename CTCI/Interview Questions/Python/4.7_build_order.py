# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

# Example:
# Input:
#       projects : a, b, c, d, e, f
#       dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

import pprint

class Graph:
    """Directed Graph Class"""
    def __init__(self, connections, projects):
        self.graph = {}
        self.num_projects = 0
        self.add_connections(connections, projects)

    def add_connections(self, connections, projects):
        for node1, node2 in connections:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node2].append(node1)
        for project in projects:
            self.num_projects += 1
            if project not in self.graph:
                self.graph[project] = []

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph)) # Casting to dict() just to make output cleaner

    def remove_node_from_dependencies(self, node_to_remove):
        for node in self.graph:
            if node_to_remove in self.graph[node]:
                self.graph[node].remove(node_to_remove)

    def has_dependencies(self):
        for node in self.graph:
            if len(self.graph[node]) > 0:
                return True
        return False

    def build_order(self):
        build_order = []
        removed_nodes = []
        while len(removed_nodes) < self.num_projects:
            for node in self.graph:
                if node not in removed_nodes and self.graph[node] == []:
                    build_order.append(node)
                    self.remove_node_from_dependencies(node)
                    removed_nodes.append(node)
        if self.has_dependencies():
            return []
        return build_order


connections = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
projects = ['a', 'b', 'c', 'd', 'e', 'f']
# connections = [('f', 'a'), ('f', 'c'), ('f', 'b'), ('c', 'a'), ('b', 'a'), ('a', 'e'), ('b', 'e'), ('d', 'g')]
projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
graph = Graph(connections, projects)
pprint.PrettyPrinter().pprint(graph.graph)
print(graph.build_order())
# pprint.PrettyPrinter().pprint(graph.graph)
