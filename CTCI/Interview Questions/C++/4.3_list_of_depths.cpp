// Given a binary tree, design an algorithm which creates a linkedlist of all the nodes at each depth (e.g if you have a tree with depth D, you'll have D linked lists)
// Page 67

#include <iostream>
#include <vector>
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
    void insert(LinkedListNode *new_node){
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
    BinaryTreeNode * head = nullptr;
public:
    BinaryTree(){
        head = new BinaryTreeNode(10);
    }
};

int main(){
    LinkedList ll;
    LinkedListNode *node_a = new LinkedListNode(5);
    LinkedListNode *node_b = new LinkedListNode(6);
    LinkedListNode *node_c = new LinkedListNode(7);
    LinkedListNode *node_d = new LinkedListNode(8);
    ll.insert(node_a);
    ll.insert(node_b);
    ll.insert(node_c);
    ll.insert(node_d);
    ll.print();

    /**
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
}
