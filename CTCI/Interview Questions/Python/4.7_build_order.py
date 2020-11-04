# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

# Example:
# Input:
#       projects : a, b, c, d, e, f
#       dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

import pprint

class Graph:
    """Directed Graph Class"""
    def __init__(self, connections, projects, reverse=False):
        self.graph = {}
        self.num_projects = 0
        self.add_connections(connections, projects, reverse)

    def add_connections(self, connections, projects, reverse):
        if reverse: # Used in DFS solution.
            for node1, node2 in connections:
                if node1 not in self.graph:
                    self.graph[node1] = []
                self.graph[node1].append(node2)
        else:
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

    # Solution 1
    # Use graph notation, and remove nodes which do not have any dependencies, i.e. incoming nodes.
    # If all nodes have been dealt with and there are dependencies left, return error.
    # Time Complexity: O(p + d) where p is the no. of projects, d is the no. of dependencies
    def get_build_order(self):
        build_order = []
        num_removed = 0
        while num_removed < self.num_projects:
            for node in self.graph:
                if node not in build_order and self.graph[node] == []:
                    build_order.append(node)
                    self.remove_node_from_dependencies(node)
                    num_removed += 1
        if self.has_dependencies():
            return []
        return build_order

    def get_unvisited_neighbour(self, node, visited):
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                return neighbour
        return None

    def choose_random_unvisited_node(self, visited):
        for node in self.graph.keys():
            if node not in visited:
                return node
        return None

    # Solution 2
    # Using DFS. Traverse until a node w/o neighbours or w/o unvisitd neighbours is seen. At the point, we know that it's the last to get added to the build order since no other projects depend on this. So add to build order. We'll reverse the build order at the end.
    # Time Complexity: O(p + d) where p is the no. of projects, d is the no. of dependencies
    # Space Complexity: O(p)
    def get_build_order_dfs(self):
        # Solution doesn't account for nodes which cannot be built. This problem for whatever reason was so frustrating that I'm annoyed and will not be proceeding with implementing it in C++
        build_order = []
        stack = []
        visited = []
        node = self.choose_random_unvisited_node(visited)
        stack.append(node)
        visited.append(node)
        while len(stack) > 0:
            neighbour = self.get_unvisited_neighbour(stack[-1], visited)
            if neighbour is not None:
                stack.append(neighbour)
                visited.append(neighbour)
            else:
                build_order.append(stack.pop())
            if len(stack) == 0:
                node = self.choose_random_unvisited_node(visited)
                if node is not None:
                    stack.append(node)
                    visited.append(node)
        return build_order[::-1]

connections = [('f', 'a'), ('f', 'c'), ('f', 'b'), ('c', 'a'), ('b', 'a'), ('a', 'e'), ('b', 'e'), ('d', 'g')] # ['e', 'g', 'a', 'd', 'c', 'b', 'f']
projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# connections = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')] # ['e', 'f', 'b', 'a', 'd', 'c']
# projects = ['a', 'b', 'c', 'd', 'e', 'f']
graph = Graph(connections, projects, reverse=False)
pprint.PrettyPrinter().pprint(graph.graph)
print(graph.get_build_order())
# print(graph.get_build_order_dfs())
# pprint.PrettyPrinter().pprint(graph.graph)
