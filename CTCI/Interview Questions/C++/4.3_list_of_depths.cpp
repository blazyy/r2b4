// Given a binary tree, design an algorithm which creates a linkedlist of all the nodes at each depth (e.g if you have a tree with depth D, you'll have D linked lists)
// Page 67

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

struct LinkedListNode{
    int val;
    LinkedListNode * next = nullptr;
    LinkedListNode(int value){
        val = value;
    }
};
class LinkedList{
private:
    LinkedListNode * head = nullptr;
    int size = 0;
public:
    void insert(int value){
        LinkedListNode * new_node = new LinkedListNode(value);
        if(head == nullptr) head = new_node;
        else{
            LinkedListNode * current = head;
            while(current -> next)
                current = current -> next;
            current -> next = new_node;
        }
        size++;
    }
    int get_size(){
        return size;
    }
    void print(){
        LinkedListNode *current = head;
        while(current){
            cout << current -> val << " ";
            current = current -> next;
        }
        cout << endl;
    }
    LinkedListNode * get_head(){
        return head;
    }
};

struct BinaryTreeNode{
    int val;
    BinaryTreeNode *left = nullptr;
    BinaryTreeNode *right = nullptr;
    BinaryTreeNode(int value){
        val = value;
    }
};
class BinaryTree{
private:
    BinaryTreeNode * root = nullptr;
    vector <BinaryTreeNode *> visited;
public:
    BinaryTree(){
        root = new BinaryTreeNode(10);
        populate_tree();
    }
    void populate_tree(){
        /**
                                Replicating this random tree.
                                ______________10___________
                              /                           \
                      _______22_____                   ____11________
                    /              \                 /              \
                 _28__            _26           ___19            ___2
               /     \          /    \        /     \         /
              17      9        25     23      4      21    _29
             /       / \      /        \      \          /    \
            6       5   3    7          8      20        13    1

        */

        // Yes. I know this looks bad. I'm doing this because unlike Python there's no library to print
        // out a tree, so I can't verify the answer at a glance if I use randomly generated numbers for my nodes.
        root -> left = new BinaryTreeNode(22);
        root -> left -> left = new BinaryTreeNode(28);
        root -> left -> left -> left = new BinaryTreeNode(17);
        root -> left -> left -> left -> left = new BinaryTreeNode(6);
        root -> left -> left -> right = new BinaryTreeNode(9);
        root -> left -> left -> right -> left = new BinaryTreeNode(5);
        root -> left -> left -> right -> right = new BinaryTreeNode(3);
        root -> left -> right = new BinaryTreeNode(26);
        root -> left -> right -> left = new BinaryTreeNode(25);
        root -> left -> right -> left -> left = new BinaryTreeNode(7);
        root -> left -> right -> right = new BinaryTreeNode(23);
        root -> left -> right -> right -> right = new BinaryTreeNode(28);
        root -> right = new BinaryTreeNode(11);
        root -> right -> left = new BinaryTreeNode(19);
        root -> right -> left -> left = new BinaryTreeNode(4);
        root -> right -> left -> left -> right = new BinaryTreeNode(20);
        root -> right -> left -> right = new BinaryTreeNode(21);
        root -> right -> right = new BinaryTreeNode(2);
        root -> right -> right -> left = new BinaryTreeNode(29);
        root -> right -> right -> left -> left = new BinaryTreeNode(13);
        root -> right -> right -> left -> right = new BinaryTreeNode(1);
    }
    BinaryTreeNode * get_unvisited_child(BinaryTreeNode * node){
        if(node -> left != nullptr and find(visited.begin(), visited.end(), node -> left) == visited.end()) return node -> left;
        if(node -> right != nullptr and find(visited.begin(), visited.end(), node -> right) == visited.end()) return node -> right;
        return nullptr;
    }
    void add_to_visited(BinaryTreeNode * node){
        visited.push_back(node);
    }
    BinaryTreeNode * get_root(){
        return root;
    }
};

// Solution 1
// DFS
// Number of linked lists depends on the length. At any stage of DFS, the depth can be found by looking at the number of elements currently in the stack. We use this number as an index for the list of linkedlists and insert new nodes accordingly.
// Time Complexity: O(n)
// Space Complexity: O(n) if iterative (which it is.) If recursive, O(h) where h is max depth of tree.
// Note: Time and space complexities might not be accurate since I'm very rusty on graphs and graph traversals.
vector <LinkedList *> return_list_of_depths_dfs (BinaryTree * tree){
    if(tree -> get_root() == nullptr)
        return vector <LinkedList *> {};
    int current_depth = 0;
    BinaryTreeNode * current = tree -> get_root();
    stack <BinaryTreeNode *> node_stack;
    node_stack.push(current);
    tree -> add_to_visited(current);
    vector <LinkedList *> linked_lists = {new LinkedList};
    linked_lists[current_depth] -> insert(current -> val);
    while(node_stack.size() > 0){
        current = tree -> get_unvisited_child(node_stack.top()); // I have a feeling that this isn't very OOP-like. Oh well.
        if(current == nullptr)
            node_stack.pop();
        else{
            node_stack.push(current);
            tree -> add_to_visited(current);
            current_depth = node_stack.size() - 1;
            if(current_depth >= linked_lists.size()){
                LinkedList * new_linked_list = new LinkedList;
                linked_lists.push_back(new_linked_list);
            }
            linked_lists[current_depth] -> insert(current -> val);
        }
    }
    return linked_lists;
}
// Solution 2
// BFS
// Getting the depth is not as straightforward as it is for DFS, but still not hard. The depth, starting from 0, is only increased when all neighbours of all nodes in the queue have been enqueued. We do this using a counter and a while loop.
// Note: BFS for trees, AKA level order traversal, does not need to use the visited property since trees do not have cycles and we deal with all children at the same time unlike DFS. Also, instead of getting all neighbours of a certain node, we can just enqueue the left and right childs since it's a binary tree.
// Time Complexity: O(n)
// Space Complexity: O(n)
// Note: Time and space complexities might not be accurate since I'm very rusty on graphs and graph traversals.
vector <LinkedList *> return_list_of_depths_bfs(BinaryTree * tree){
    if(tree -> get_root() == nullptr)
        return vector <LinkedList *> {};
    int nodes_in_current_level, current_depth = 0;
    BinaryTreeNode * current = tree -> get_root();
    queue <BinaryTreeNode *> node_queue;
    vector <LinkedList *> linked_lists = {};
    node_queue.push(current);
    while(node_queue.size()){
        nodes_in_current_level = node_queue.size();
        while(nodes_in_current_level){ //  Increase depth only after dealing with all nodes in the current level
            current = node_queue.front();
            node_queue.pop();
            if(current_depth >= linked_lists.size()) linked_lists.push_back(new LinkedList);
            linked_lists[current_depth] -> insert(current -> val);
            if(current -> left) node_queue.push(current -> left);
            if(current -> right) node_queue.push(current -> right);
            nodes_in_current_level--;
        }
        current_depth++;
    }
    return linked_lists;
}

void print_list_of_lists(vector <LinkedList *> linked_lists){
    for(auto linked_list : linked_lists){
        LinkedListNode * current = linked_list -> get_head();
        while(current){
            cout << current -> val << " ";
            current = current -> next;
        }
        cout << endl;
    }
}

int main(){
    BinaryTree * bt = new BinaryTree();
    vector <LinkedList *> linked_lists = return_list_of_depths_dfs(bt);
    print_list_of_lists(linked_lists);
    linked_lists = return_list_of_depths_bfs(bt);
    print_list_of_lists(linked_lists);
}
