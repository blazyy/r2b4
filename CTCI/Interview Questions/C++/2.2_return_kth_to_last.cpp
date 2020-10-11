// Implement an algorithm to find the kth to last element of a singly linked list

// Page 63

#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

struct Node{
    int data;
    Node * next = NULL;
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
    void set_head(Node * new_head){
        head = new_head;
    }
    Node * get_head(){
        return head;
    }
    int get_size(){
        return size;
    }
};

vector <int> create_random_vect(int num_elements){
    vector <int> return_vect;
    for(int i = 0; i < num_elements; i++)
        return_vect.push_back(rand() % (num_elements/2 + 1));
    return return_vect;
}

// Solution 1
// Traverse through list until index (n-k) is visited.
// This solution assumes size of list is already known.
// Time Complexity: O(n), Space Complexity: O(1)
int return_kth_to_last_1(LinkedList * ll, int k){
    int kth_to_last_idx = (*ll).get_size() - k;
    Node * current = (*ll).get_head();
    int idx = 0;
    int return_ele;
    while(current){
        if(idx == kth_to_last_idx){
            return_ele = current -> data;
            break;
        }
        idx++;
        current = current -> next;
    }
    return return_ele;
}

// Solution 2
// Recursive solution - doesn't return kth-from-last, only prints.
// List size not known.
// Time Complexity: O(n), Space Complexity: O(n) (since recursive)
int return_kth_to_last_2(Node * node, int k){
    if(node == NULL) return 0;
    int index = return_kth_to_last_2(node -> next, k) + 1;
    if(index == k)
        cout << node -> data << endl;
    return index;
}

// Solution 3
// Iterative - size of list unknown. Instead of two passes(one for finding size and then one for finding kth-to-last), do in one pass
// Time Complexity: O(n), Space Complexity: O(1)
int return_kth_to_last_3(LinkedList * ll, int k){
    int idx = 1; // Considering last element as index 1 (instead of 0) when read in reverse
    int return_ele;
    Node * fast = (*ll).get_head();
    Node * slow = NULL;
    while(fast){
        if(slow) slow = slow -> next;
        if(idx == k) slow = (*ll).get_head();
        if(fast -> next == NULL){
            return_ele = slow -> data;
            break;
        }
        idx++;
        fast = fast -> next;
    }
    return return_ele;
}

int main(void){
    srand(time(NULL)); // Using time as seed for RNG
    int num_elements = 10;
    vector <int> random_vect = create_random_vect(num_elements);
    LinkedList * ll = new LinkedList;
    (*ll).fill(random_vect);
    (*ll).print();
    cout << return_kth_to_last_1(ll, 3) << endl;
    return_kth_to_last_2((*ll).get_head(), 3);
    cout << return_kth_to_last_3(ll, 3) << endl;

}
