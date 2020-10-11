// Write code to remove duplicates from an unsorted linked list

// Page 63

#include <iostream>
#include <vector>
#include <set>
#include <ctime>
using namespace std;

struct Node{
    int data;
    Node * next = NULL;
};

class LinkedList{
private:
    Node * head = NULL;
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
};

vector <int> create_random_vect(int num_elements){
    vector <int> return_vect;
    for(int i = 0; i < num_elements; i++)
        return_vect.push_back(rand() % (num_elements/2 + 1));
    return return_vect;
}

// Solution 1
// Use set to store visited elements
// Time Complexity: O(n), Space Complexity: O(n)
void remove_dups_1(LinkedList * ll){
    if(ll == NULL || (*ll).get_head() == NULL) return;
    set <int> visited;
    Node * current = (*ll).get_head();
    Node * prev = current;
    while(current){
        if(visited.find(current -> data) != visited.end())
            prev -> next = current -> next;
        else{
            visited.insert(current -> data);
            prev = current; // Only change previous if not a duplicate, because after setting prev.next to current.next, prev should stay at prev and not move to prev.next which is the current deleted node.
        }
        current = current -> next;
    }
}

// Solution 2
// Once at a node, traverse through the remaining right part of the linked list and remove if that node's value is seen again
// Time Complexity: O(n^2), Space Complexity: O(1)
void remove_dups_2(LinkedList * ll){
    if(ll == NULL || (*ll).get_head() == NULL) return;
    Node * current = (*ll).get_head();
    Node * traverser;
    Node * prev;
    while(current){
        prev = current;
        traverser = current -> next;
        while(traverser){
            if(current -> data == traverser -> data)
                prev -> next = traverser -> next;
            else prev = traverser; // Only change previous if not a duplicate, because after setting prev.next to traverser.next, prev should stay at prev and not move to prev.next which is the current deleted node.
            traverser = traverser -> next;
        }
        current = current -> next;
    }
}

int main(void){
    srand(time(NULL)); // Using time as seed for RNG
    int num_elements = 10;

    vector <int> random_vect = create_random_vect(num_elements);
    LinkedList * ll1 = new LinkedList;
    (*ll1).fill(random_vect);
    (*ll1).print();
    remove_dups_1(ll1);
    (*ll1).print();

    cout << endl;

    random_vect = create_random_vect(num_elements);
    LinkedList * ll2 = new LinkedList;
    (*ll2).fill(random_vect);
    (*ll2).print();
    remove_dups_2(ll2);
    (*ll2).print();
}
