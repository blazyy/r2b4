// Write an algorithm to find the "next" node, i.e. the inorder successor of a given node in a BST. You may assume that each node has a link to its parent.

#include <iostream>
using namespace std;

struct Node{
    int val;
    Node *left = nullptr;
    Node *right = nullptr;
    Node *parent = nullptr;
    Node(int value, Node *par){
        val = value;
        parent = par;
    }
};

class BinaryTree{
private:
    Node *root = nullptr;
    Node *node1 = nullptr;
    Node *node2 = nullptr;
    Node *node3 = nullptr;
public:
    BinaryTree(){
    /* Replicating the following tree. Contains nodes that can help verify if all the 3 cases for finding a successor work properly.
                                                _________26______
                                              /                 \
                                       ______9               ____29
                                     /       \             /
                                 __4__       10___        27
                               /     \            \        \
                             2       7           _25       28
                            / \     / \        /
                          0   3   5   8      15

               We'll find the successors for 9, 25, and 15. These cover the 3 cases.

  */
        root = new Node(26, nullptr);
        node1 = new Node(9, root);
        root -> left = node1;
        root -> right = new Node(29, root);
        root -> left -> left = new Node(4, root -> left);
        root -> left -> left -> left = new Node(2, root -> left -> left);
        root -> left -> left -> left -> left = new Node(0, root -> left -> left -> left);
        root -> left -> left -> left -> right = new Node(3, root -> left -> left -> left);
        root -> left -> left -> right = new Node(7, root -> left -> left);
        root -> left -> left -> right -> left = new Node(5, root -> left -> left -> right);
        root -> left -> left -> right -> right = new Node(8, root -> left -> left -> right);
        root -> left -> right = new Node(10, root -> left);
        node2 = new Node(25, root -> left -> right);
        root -> left -> right -> right = node2;
        node3 = new Node(15, root -> left -> right -> right);
        root -> left -> right -> right -> left = node3;
        root -> right = new Node(29, root);
        root -> right -> left = new Node(27, root -> right);
        root -> right -> left -> right = new Node(28, root -> right -> left);
    }
    void inorder(Node *root){
        if(root == nullptr) return;
        inorder(root -> left);
        cout << root -> val << " ";
        inorder(root -> right);
    }
    Node * get_root(){
        return root;
    }
    // Solution
    // Using the following rules to find the successor:
    // 1) If the node has a right child, then the successor is the smallest key in the right subtree.
    // 2) If the node has no right child and is the left child of its parent, then the parent is the successor.
    // 3) If the node has no right child and is the right child of its parent, then the successor to this node is the successor of its parent, excluding this node.
    Node * find_succesor(Node * node){
        if(node == nullptr) return nullptr;
        Node *succ = nullptr;
        if(node -> right != nullptr){
            Node *current = node -> right;
            while(current -> left) current = current -> left;
            succ = current;
        }
        else{
            Node *parent = node -> parent;
            if(parent != nullptr)
                if(parent -> left == node) succ = parent; // If node is the left child of its parent
                else if(parent -> right == node){
                    parent -> right = nullptr; // Setting current node to be None. Read rules above.
                    succ = find_succesor(parent);
                    parent -> right = node; // Setting it back
                }
        }
        return succ;
    }
    Node * get_node1(){
        return node1;
    }
    Node * get_node2(){
        return node2;
    }
    Node * get_node3(){
        return node3;
    }
};

int main(void){
    BinaryTree bt;
    cout << "Successor of " << bt.get_node1() -> val << " is " << bt.find_succesor(bt.get_node1()) -> val << endl;
    cout << "Successor of " << bt.get_node2() -> val << " is " << bt.find_succesor(bt.get_node2()) -> val << endl;
    cout << "Successor of " << bt.get_node3() -> val << " is " << bt.find_succesor(bt.get_node3()) -> val << endl;
}
