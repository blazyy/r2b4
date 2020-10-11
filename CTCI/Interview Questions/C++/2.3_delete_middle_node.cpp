// Implement an algorithm to delete a node in the midddle (i.e. any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node

// Page 63

#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

struct Node{
    int data;
    Node * next = NULL;

    void set_next(Node * next_node){
        next = next_node;
    }
    Node * get_next(){
        return next;
    }
    void set_data(int new_data){
        data = new_data;
    }
    int get_data(){
        return data;
    }
};

class LinkedList{
private:
    Node * head = NULL;
    int size = 0;
public:
    void append(int data){
        Node * new_node = new Node;
        new_node -> data = data;
        if(head == NULL)
            head = new_node;
        else{
            Node * current = head;
            while(current -> next)
                current = current -> next;
            current -> next = new_node;
        }
        size++;
    }
    void fill(vector <int> elements){
        for(auto element : elements)
            append(element);
    }
    void print(){
        Node * current = head;
        while(current){
            cout << current -> data << " ";
            current = current -> next;
        }
        cout << endl;
    }
    int get_size(){
        return size;
    }
    Node * get_head(){
        return head;
    }
};

vector <int> create_random_vect(int num_elements){
    vector <int> return_vect;
    for(int i = 1; i < num_elements + 1; i++)
        return_vect.push_back(rand() % num_elements + 1);
    return return_vect;
}

// Solution 1
// Set mid's data to next data, and set mid's next to next's next
// Time Complexity: O(n), Space Complexity: O(1)
void delete_middle_node(Node * mid_node){
    if(mid_node == NULL || mid_node -> next == NULL) return;
    mid_node -> data = mid_node -> next -> data;
    mid_node -> next = mid_node -> next -> next;
}


int main(void){
    srand(time(NULL)); // Using time as seed for RNG
    int num_elements = 10;
    vector <int> random_vect = create_random_vect(num_elements);
    LinkedList * ll = new LinkedList;
    (*ll).fill(random_vect);
    (*ll).print();

    Node * mid_node = (*ll).get_head();
    int i = 1;
    while(i < num_elements / 2){
        i++;
        mid_node = mid_node -> next;
    }
    cout << "Removing middle node (" << mid_node -> data << ")" << endl;
    delete_middle_node(mid_node);
    (*ll).print();
}
