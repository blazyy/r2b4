// Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of thr two subtrees of any node never differ by more than one.

#include <iostream>
#include <vector>
#include <stdlib.h>  // for abs()
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
    Node *root = nullptr;
public:
    BinaryTree(bool balanced){
        if(balanced){
            root = new Node(5);
            root -> left = new Node(6);
            root -> right = new Node(7);
            root -> left -> left = new Node(8);
            root -> left -> right = new Node(9);
            root -> right -> left = new Node(10);
            root -> right -> right = new Node(11);
        } else{
            root = new Node(5);
            root -> left = new Node(6);
            root -> left -> left = new Node(7);
        }
    }
    void inorder(Node *root){
        if(!root) return;
        inorder(root -> left);
        cout << root -> val << " ";
        inorder(root -> right);
    }
    Node * get_root(){
        return root;
    }
    int get_height(Node * root){
        if(root == nullptr) return -1;
        return max(get_height(root -> left), get_height(root -> right)) + 1;
    }
    // Solution 1
    // Recurse through tree, and for each node, compute the heights of each subtree
    // Time Complexity: O(n log n), since each node is 'touched' once per node above it
    // Space Complexity: O(n)
    bool is_balanced_1(Node *root){
        if(root == nullptr) return true;
        int height_diff = abs(get_height(root -> left) - get_height(root -> right));
        if(height_diff > 1) return false;
        else{
            return is_balanced_1(root -> left) && is_balanced_1(root -> right);
        }
    }
    int check_height(Node *root){
        if(root == nullptr)
            return -1;
        int left_height = check_height(root -> left);
        if(left_height == INT_MIN)
            return INT_MIN;
        int right_height = check_height(root -> right);
        if(right_height == INT_MIN)
            return INT_MIN;
        if(abs(left_height - right_height) > 1)
            return INT_MIN;
        else
            return max(left_height, right_height) + 1;
    }
    bool is_balanced_2(Node * root){
        return check_height(root) != INT_MIN;
    }
};

int main(void){
    BinaryTree balanced_tree(true);
    BinaryTree unbalanced_tree(false);
    cout << balanced_tree.is_balanced_1(balanced_tree.get_root()) << endl;
    cout << balanced_tree.is_balanced_2(balanced_tree.get_root()) << endl;
    cout << unbalanced_tree.is_balanced_1(unbalanced_tree.get_root()) << endl;
    cout << unbalanced_tree.is_balanced_2(unbalanced_tree.get_root()) << endl;
}
