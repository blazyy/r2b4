#include <iostream>
#include <vector>
using namespace std;

class BinaryTree{
private:
    int root;
    BinaryTree * left = NULL;
    BinaryTree * right = NULL;
public:
    BinaryTree(int root_val){
        // constructor
        root = root_val;
    }
    void insert_right(int value){
        BinaryTree * new_node = new BinaryTree(value);
        new_node -> root = value;
        if(right == NULL)
            right = new_node;
        else{
            new_node -> right = right;
            right = new_node;
        }
    }
    BinaryTree * get_right(){
        return right;
    }
    void insert_left(int value){
        BinaryTree * new_node = new BinaryTree(value);
        new_node -> root = value;
        if(left == NULL)
            left = new_node;
        else{
            new_node -> left = left;
            left = new_node;
        }
    }
    BinaryTree * get_left(){
        return left;
    }
    void set_root(int value){
        root = value;
    }
    int get_root(){
        return root;
    }
};

int main(void){
    BinaryTree tree(69);
}
