#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <time.h>
using namespace std;

struct Node{
    int key;
    string value;
    struct Node * left = NULL;
    struct Node * right = NULL;
    struct Node * parent = NULL;
    bool has_no_children(){
        if(left == NULL && right == NULL)
            return true;
        return false;
    }
    bool has_one_child(){
        if(left == NULL && right != NULL)
            return true;
        if(left != NULL and right == NULL)
            return true;
        return false;
    }
    bool is_left_child(){
        // This function works since BSTs cannot have duplicate keys.
        if(key == parent -> left -> key)
            return true;
        return false;
    }
    bool is_right_child(){
        // This function works since BSTs cannot have duplicate keys.
        if(key == parent -> right -> key)
            return true;
        return false;
    }
    bool has_left_child(){
        if(left != NULL)
            return true;
        return false;
    }
    bool has_right_child(){
        if(right != NULL)
            return true;
        return false;
    }
};

class BinarySearchTree{
private:
    struct Node * root = NULL;
public:
    struct Node * get_root(){
        return root;
    }
    void insert_node(int key, string value){
        struct Node * new_node = new Node;
        new_node -> key = key;
        new_node -> value = value;
        if(root == NULL) // If tree is empty
            root = new_node;
        else{
            struct Node * current = root;
            while(current){
                if(key == current -> key){
                    current -> value = value;
                    break;
                }
                else if(key < current -> key){
                    if(current -> left == NULL){
                        current -> left = new_node;
                        new_node -> parent = current;
                        break;
                    }
                    else
                        current = current -> left;
                }
                else{
                    if(current -> right == NULL){
                        current -> right = new_node;
                        new_node -> parent = current;
                        break;
                    }
                    else
                        current = current -> right;
                }
            }
        }
    }
    bool contains(int key){
        struct Node * current = root;
        while(current){
            if(key == current -> key)
                return true;
            else if(key < current -> key)
                current = current -> left;
            else
                current = current -> right;
        }
        return false;
    }
    struct Node * find_min(struct Node * node){
        struct Node * current = node;
        while(current -> left)
            current = current -> left;
        return current;
    }
    struct Node * find_successor(struct Node * node){
        // A successor cannot have more than 1 children in a BST.
        struct Node * successor = NULL;
        if((*node).has_right_child()){
            successor = find_min(node -> right);
        }
        else{
            if((*node).is_left_child())
                successor = node -> parent;
            else{ // If node has no right child and is a right child of it's parent, it's successor is it's parent's successor excluding itself.
                node -> parent -> right = node -> right; // Temporarily removing node.
                successor = find_successor(node -> parent);
                node -> parent -> right = node;
            }
        }
        return successor;
    }
    void delete_node(int key){
        if(!contains(key)){
            cout << "KeyError: " << key << endl;
            exit(0);
        }
        else{
            struct Node * current = root;
            while(current){
                if(key == current -> key){
                    // current -> has_no_children() didn't feel right. So I did this.
                    if((*current).has_no_children()){ // If node to delete has no children
                        if(current -> parent == NULL){ // If node to delete is root
                            root = NULL;
                        }
                        else{
                            if((*current).is_left_child())
                                current -> parent -> left = NULL;
                            else
                                current -> parent -> right = NULL;
                        }
                        break;
                    }
                    else if((*current).has_one_child()){ // If node to delete has one child
                        if(current -> parent == NULL){ // If node to delete is root
                            if((*current).has_left_child()){
                                root = current -> left;
                                root -> parent = NULL;
                            }
                            else{
                                root = current -> right;
                                root -> parent = NULL;
                            }
                            break;
                        }
                        else{
                            if((*current).has_left_child()){
                                current -> left -> parent = current -> parent;
                                if((*current).is_left_child())
                                    current -> parent -> left = current -> left;
                                else
                                    current -> parent -> right = current -> left;
                            }
                            else{
                                current -> right -> parent = current -> parent;
                                if((*current).is_left_child())
                                    current -> parent -> left = current -> right;
                                else
                                    current -> parent -> right = current -> right;
                            }
                        }
                        break;
                    }
                    else{ // If node to delete has two children
                        cout << "Node to delete has two children!" << endl;
                        struct Node * successor = find_successor(current);
                        current -> key = successor -> key;
                        current -> value = successor -> value;
                        // A successor will not have 2 children. Either 0 or 1.
                        if((*successor).has_no_children()){
                            if((*successor).is_left_child())
                                successor -> parent -> left = NULL;
                            else
                                successor -> parent -> right = NULL;
                        }
                        else{
                            if((*successor).has_left_child()){
                                if((*successor).is_left_child())
                                    successor -> parent -> left = successor -> left;
                                else
                                    successor -> parent -> right = successor -> left;
                            }
                            else{
                                if((*successor).is_left_child())
                                    successor -> parent -> left = successor -> right;
                                else
                                    successor -> parent -> right = successor -> right;
                            }
                        }
                        break;
                    }
                }
                else if(key < current -> key)
                    current = current -> left;
                else
                    current = current -> right;
            }
        }
    }
};

void print_inorder(struct Node * node){
    if(node != NULL){
        print_inorder(node -> left);
        cout << node -> key << " ";
        print_inorder(node -> right);
    }
}

void print_array(unordered_set <int> arr, int size){
    for(auto num: arr)
        cout << num << " ";
}

int main(void){
    srand(time(0));
    BinarySearchTree bst; int size = 10;
    unordered_set <int> arr, rand_idxs;
    vector <int> int_arr;
    while(arr.size() <= size)
        arr.insert(rand() % 100);
    for(auto num: arr){
        bst.insert_node(num, "placeholder_string");
        int_arr.push_back(num);
    }
    while(rand_idxs.size() < size/2)
        rand_idxs.insert(rand() % size);
    cout << "Array:\t\t"; print_array(arr, size); cout << endl;
    cout << "Inorder:\t"; print_inorder(bst.get_root()); cout << endl;
    for(auto idx: rand_idxs){
        cout << "Deleting " << int_arr[idx] << endl;
        bst.delete_node(int_arr[idx]);
    }
    cout << "New Inorder:\t"; print_inorder(bst.get_root()); cout << endl;
}
