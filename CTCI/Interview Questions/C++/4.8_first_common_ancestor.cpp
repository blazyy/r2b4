// Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This not not necessarily a binary search tree.

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

struct Node{
    int val;
    Node *left = nullptr;
    Node *right = nullptr;
    Node(int value){
        val = value;
    }
};

class BinaryTree{
private:
    Node *root, *node1, *node2, *node3, *node4, *node5, *node6;
    vector <Node *> node1s; // Used only for verifying correctness of algorithm
    vector <Node *> node2s; // Same
public:
    BinaryTree(){
        root = new Node(10);
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

        node1 = new Node(22); node1s.push_back(node1);
        node2 = new Node(11); node2s.push_back(node2);
        node3 = new Node(28); node1s.push_back(node3);
        node4 = new Node(21); node2s.push_back(node4);
        node5 = new Node(17); node1s.push_back(node5);
        node6 = new Node(8); node2s.push_back(node6);
        root -> left = node1;
        root -> left -> left = node3;
        root -> left -> left -> left = node5;
        root -> left -> left -> left -> left = new Node(6);
        root -> left -> left -> right = new Node(9);
        root -> left -> left -> right -> left = new Node(5);
        root -> left -> left -> right -> right = new Node(3);
        root -> left -> right = new Node(26);
        root -> left -> right -> left = new Node(25);
        root -> left -> right -> left -> left = new Node(7);
        root -> left -> right -> right = new Node(23);
        root -> left -> right -> right -> right = node6;
        root -> right = node2;
        root -> right -> left = new Node(19);
        root -> right -> left -> left = new Node(4);
        root -> right -> left -> left -> right = new Node(20);
        root -> right -> left -> right = node4;
        root -> right -> right = new Node(2);
        root -> right -> right -> left = new Node(29);
        root -> right -> right -> left -> left = new Node(13);
        root -> right -> right -> left -> right = new Node(1);
    }
    Node * get_root(){
        return root;
    }
    // Solution
    // Traverse the entire tree, in postorder fashion. How the algorithm works is for each subtree, it returns a value. It returns NULL if the node we're looking for isn't in the subtree, else, it returns the node itself. When we know that left and right subtrees contain a value that is NOT NULL, we know that we have found the two nodes we're looking for, and that the current node we're at is the first common ancestor.
    Node * find_common_ancestor(Node *root, Node *node1, Node *node2){
        if(root == nullptr || root == node1 || root == node2) return root;
        Node *left = find_common_ancestor(root -> left, node1, node2);
        Node *right = find_common_ancestor(root -> right, node1, node2);
        if(left == nullptr && right == nullptr) return nullptr;
        if(left == nullptr) return right;
        if(right == nullptr) return left;
        return root; // if both are not null, this is our result
    }
    void verify_fca_algorithm(){
        for(int i = 0; i < 3; i++)
            cout << "FCA of " << node1s[i] -> val << " and " << node2s[i] -> val << " is " << find_common_ancestor(root, node1s[i], node2s[i]) -> val << endl;
    }
};
int main(){
    BinaryTree * bt = new BinaryTree();
    bt -> verify_fca_algorithm();
}
