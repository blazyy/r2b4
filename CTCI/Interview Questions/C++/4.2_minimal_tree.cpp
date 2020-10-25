// Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
// Page 75

#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
using namespace std;

struct Node{
    int data;
    Node *left = nullptr;
    Node *right = nullptr;
    Node(int newdata){
        data = newdata;
    }
};

class BinarySearchTree{
private:
    Node * root = nullptr;
public:
    BinarySearchTree(vector <int> &values){
        construct_bst(values, 0, values.size() - 1);
    }
    // Solution
    // Kinda like binary search. Pretty simple solution.
    // Time Complexity: O(n)
    Node * construct_bst(vector <int> &elements, int start, int end){
        if(end < start) return nullptr;
        int mid = (start + end) / 2;
        Node * new_node = new Node(elements[mid]);
        if(root == nullptr) root = new_node;
        new_node -> left = construct_bst(elements, start, mid - 1);
        new_node -> right = construct_bst(elements, mid + 1, end);
        return new_node;
    }
    Node * get_root(){
        return root;
    }
};

void inorder(Node * node){
    if(node == NULL) return;
    inorder(node -> left);
    cout << node -> data << " ";
    inorder(node -> right);
}

vector <int> gen_array(int n, int upper_bound=100){
    if(n >= upper_bound) return vector <int> {};
    vector <int> elements;
    while(elements.size() < n){
        int rand_num = rand() % 100;
        if(find(elements.begin(), elements.end(), rand_num) == elements.end())
            elements.push_back(rand_num);
    }
    sort(elements.begin(), elements.end());
    return elements;
}

int main(void){
    srand(time(NULL));
    int num_elements = 10;
    vector <int> arr = gen_array(num_elements);
    BinarySearchTree * bst = new BinarySearchTree(arr);
    inorder(bst -> get_root());
}
