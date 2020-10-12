// Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see example below). The partition element x can appear anywhere in the "right partition". It does not need to appear between the left and right partitions.

// Input  = 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
// Output = 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

// Page 64

#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm> // For sort function
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
    Node * get_head(){
        return head;
    }
};

vector <int> create_random_vect(int num_elements){
    vector <int> return_vect;
    for(int i = 0; i < num_elements; i++)
        return_vect.push_back(rand() % (num_elements));
    return return_vect;
}

// Solution
// This can be solved with the partitioning scheme used in quicksort. In this case, it only needs to be called once.
// Time Complexity: O(n), Space Complexity: O(1)
void partition(LinkedList * ll, int pivot){
    Node * p_index = (*ll).get_head();
    Node * current = (*ll).get_head();
    while(current){
        if(current -> data < pivot){
            int temp = current -> data;
            current -> data = p_index -> data;
            p_index -> data = temp;
            p_index = p_index -> next;
        }
        current = current -> next;
    }
}

int main(void){
    srand(time(NULL)); // Using time as seed for RNG
    int num_elements = 10;
    vector <int> random_vect = create_random_vect(num_elements);
    LinkedList * ll = new LinkedList;
    (*ll).fill(random_vect);
    (*ll).print();
    sort(random_vect.begin(), random_vect.end());
    int pivot = random_vect[random_vect.size()/2]; // Choosing the middle element of sorted elements that were appeneed to the linked list.
    cout << "Pivot: " << pivot << endl;
    partition(ll, pivot);
    (*ll).print();
}
