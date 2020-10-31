// Implement a function to check if a binary tree is a binary search tree.

#include <iostream>
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
    BinaryTree(bool is_bst){
        root = new Node(20);
        root -> left = new Node(10);
        root -> right = new Node(30);
        if(is_bst) root -> left -> right = new Node(15);
        else root -> left -> right = new Node(25);
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
};

// Solution 1
// Uses the fact that when traversing a valid BST inorder, the values will be in sorted order (ascending)
// Works for most cases but if there's a misplaced node that is more than one level apart, this algorith fails to detect it. Eg:
//               20
//             /   \
//           10     30
//            \
//             25
// This function returns true for this tree, which it shouldn't.
// Time Complexity: O(n)
// Space Complexity:  O(log N) or O(h) since we may recurse up to the depth of the tree
bool validate_bst_1(Node *root, Node *prev=nullptr){
    if(root == nullptr)
        return true;
    if(!validate_bst_1(root -> left, prev))
        return false;
    if(prev != nullptr && root -> val <= prev -> val)
        return false;
    prev = root;
    if(!validate_bst_1(root -> right, prev))
        return false;
    return true;
}

bool check_bst(Node *root, Node *min, Node *max){
    if(root == nullptr) return true;
    else if((min != nullptr && root -> val >= min -> val) || (max != nullptr && root -> val <= max -> val))
    return false;
    else
    return check_bst(root -> left, root, max) && check_bst(root -> right, min, root);
}
// Solution 2
// Keeping track of min and max and each subtree and checking if the current node violates the BST property.
// Time Complexity: O(n)
// Space Complexity:  O(log N) or O(h) since we may recurse up to the depth of the tree
bool validate_bst_2(Node *root){
    return check_bst(root, nullptr, nullptr);
}

int main(void){
    BinaryTree bt(true);
    BinaryTree ibt(false);
    cout << validate_bst_1(bt.get_root()) << endl;
    cout << validate_bst_2(bt.get_root()) << endl;
    cout << validate_bst_1(ibt.get_root()) << endl; // eturns true, when answer should be false. Solution 1 isn't a complete solution.
    cout << validate_bst_2(ibt.get_root()) << endl;
}
