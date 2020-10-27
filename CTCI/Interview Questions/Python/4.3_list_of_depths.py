# Given a binary tree, design an algorithm which creates a linkedlist of all the nodes at each depth (e.g if you have a tree with depth D, you'll have D linked lists)
# Page 67

from binarytree import tree # A very useful library that I can use to generate trees on the fly. Saves me so much more time since I don't have to generate my own trees anymore. But for C++... *sigh*
visited = [] # Using this to keep track of visited nodes. The library I'm using doesn't have a visited property, so I'll have to use this.

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    def __len__(self):
        return self.size
    def __repr__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.val )
            current = current.next
        return ' '.join([str(ele) for ele in elements])

def get_unvisited_child(node):
    if node.left is not None and node.left not in visited:
        return node.left
    if node.right is not None and node.right not in visited:
        return node.right
    return None

# Solution 1
# DFS
# Number of linked lists depends on the length. At any stage of DFS, the depth can be found by looking at the number of elements currently in the stack. We use this number as an index for the list of linkedlists and insert new nodes accordingly.
# Time Complexity: O(n)
# Space Complexity: O(n) if iterative (which it is.) If recursive, O(h) where h is max depth of tree.
# Note: Time and space complexities might not be accurate since I'm very rusty on graphs and graph traversals.
def return_list_of_depths_dfs(root):
    if root is None:
        return
    current = root
    linked_lists = [LinkedList()]
    stack = [current]
    visited.append(current)
    linked_lists[0].insert(Node(current.val))
    while len(stack) > 0:
        current = get_unvisited_child(stack[-1])
        if current is None:
            stack.pop()
        else:
            stack.append(current)
            visited.append(current)
            current_depth = len(stack) - 1
            if current_depth >= len(linked_lists):
                linked_lists.append(LinkedList())
            linked_lists[current_depth].insert(Node(current.val))
    return linked_lists

# Solution 2
# BFS
# Getting the depth is not as straightforward as it is for DFS, but still not hard. The depth, starting from 0, is only increased when all neighbours of all nodes in the queue have been enqueued. We do this using a counter and a while loop.
# Note: BFS for trees, AKA level order traversal, does not need to use the visited property since trees do not have cycles and we deal with all children at the same time unlike DFS. Also, instead of getting all neighbours of a certain node, we can just enqueue the left and right childs since it's a binary tree.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Time and space complexities might not be accurate since I'm very rusty on graphs and graph traversals.
def return_list_of_depths_bfs(root):
    if root is None:
        return
    current_depth = 0
    linked_lists = []
    current = root
    queue = [current]
    while len(queue):
        nodes_in_current_level = len(queue)
        while nodes_in_current_level: # Increase depth only after dealing with all nodes in the current level
            current = queue.pop(0)
            if current_depth >= len(linked_lists):
                linked_lists.append(LinkedList())
            linked_lists[current_depth].insert(Node(current.val))
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            nodes_in_current_level -= 1
        current_depth += 1
    return linked_lists

my_tree = tree(height=4) # tree() returns the root node of the tree.
print(my_tree)
lls = return_list_of_depths_dfs(my_tree)
for ll in lls:
    print(ll)

print()

lls = return_list_of_depths_bfs(my_tree)
for ll in lls:
    print(ll)
