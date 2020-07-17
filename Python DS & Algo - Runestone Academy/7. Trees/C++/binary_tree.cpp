#include <iostream>
#include <vector>
using namespace std;

class BinaryTree{
private:
    char root;
    BinaryTree * left = NULL;
    BinaryTree * right = NULL;
public:
    void insert_right(char value){
        BinaryTree * new_node = new BinaryTree();
        if(right == NULL)
            right = new_node;
        else{
            new_node -> right = right;
            right = new_node;
        }
    }
    void insert_left(char value){
        BinaryTree * new_node = new BinaryTree();
        if(left == NULL)
            left = new_node;
        else{
            new_node -> left = left;
            left = new_node;
        }
    }
    BinaryTree * get_right(){
        return right;
    }
    BinaryTree * get_left(){
        return left;
    }
    char get_root(){
        return root;
    }
    void set_root(char value){
        root = value;
    }
};

void preorder(BinaryTree * tree){
    if(tree != NULL){
        cout << tree -> get_root() << " ";
        preorder(tree -> get_left());
        preorder(tree -> get_right());
    }
}
void inorder(BinaryTree * tree){
    if(tree != NULL){
        inorder(tree -> get_left());
        cout << tree -> get_root() << " ";
        inorder(tree -> get_right());
    }
}
void postorder(BinaryTree * tree){
    if(tree != NULL){
        postorder(tree -> get_left());
        postorder(tree -> get_right());
        cout << tree -> get_root() << " ";
    }
}

int main(void){
    BinaryTree * tree = new BinaryTree;
    tree -> set_root(1);
    tree -> insert_left(2);
    tree -> get_left() -> insert_left(3);
    tree -> get_left() -> insert_right(4);
    tree -> insert_right(5);
    tree -> get_right() -> insert_left(6);
    tree -> get_right() -> insert_right(7);
    preorder(tree);
    cout << "\n";
    inorder(tree);
    cout << "\n";
    preorder(tree);
}
