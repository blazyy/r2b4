// Given two singly linked list, determine if two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) and the jth node of the second linked list, then they are intersecting.

// Page 64

#include <iostream>
#include <vector>
using namespace std;

struct Node{
    int data;
    Node * next = NULL;
    Node(int new_data){
        data = new_data;
    }
};

class LinkedList{
private:
    Node * head = NULL;
public:
    void append(Node * new_node){
        if(head == NULL)
            head = new_node;
        else{
            Node * current = head;
            while(current -> next)
                current = current -> next;
            current -> next = new_node;
        }
    }
    void fill(vector <Node *> elements){
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

// Solution
// Traverse both lists at same speed. When we reach the end of the shorter list, it is set to the head of the longer list. When we reach the end of the longer list, we set it to the head of the shorter list. At this point, the two pointers are n nodes between each other where n is the difference in their size. (If both lists are the same size, they will intersect even before starting from the heads again) After they have been set to the respective heads, traversing the list normally will reach a point where both will meet at the same node (if intersection exists)
// To check for no intersection, just check if the tail nodes of each list are equal. If they aren't, there is no intersection.
// Time Complexity: O(m + n) where m and n are the sizes of each of the lists.
// Space Complexity: O(1)
bool are_intersecting(LinkedList list_a, LinkedList list_b){
    Node * curr_a = list_a.get_head();
    Node * curr_b = list_b.get_head();
    if(!curr_a || !curr_b) return false;
    Node * tail_a = NULL;
    Node * tail_b = NULL;
    bool has_intersection;
    while(true){
        // Lists which do not intersect have different tails
        if(tail_a && tail_b && tail_a != tail_b){
            has_intersection = false;
            break;
        }
        if(curr_a == curr_b){
            has_intersection = true;
            break;
        }
        if(curr_a -> next) curr_a = curr_a -> next;
        else{
            tail_a = curr_a;
            curr_a = list_b.get_head();
        }
        if(curr_b -> next) curr_b = curr_b -> next;
        else{
            tail_b = curr_b;
            curr_b = list_a.get_head();
        }
    }
    return has_intersection;
}

// Creating the following list:

//   3 -> 1 -> 5 -> 9
//                   \
//                    7 -> 2 -> 1
//           4 -> 6 /

int main(void){
    LinkedList list_a;
    Node * node1 = new Node(3);
    Node * node2 = new Node(1);
    Node * node3 = new Node(5);
    Node * node4 = new Node(9);
    Node * node5 = new Node(2);
    Node * node6 = new Node(1);
    Node * intersecting_node = new Node(7);
    vector <Node *> nodes = {node1, node2, node3, node4, intersecting_node, node5, node6};
    list_a.fill(nodes);

    LinkedList list_b;
    Node * node7 = new Node(4);
    Node * node8 = new Node(6);
    nodes = {node7, node8, intersecting_node};
    list_b.fill(nodes);

    cout << are_intersecting(list_a, list_b) << endl;

    LinkedList list_c;
    Node * node9 = new Node(3);
    Node * node10 = new Node(4);
    Node * node11 = new Node(5);
    nodes = {node9, node10, node11};
    list_c.fill(nodes); 

    cout << are_intersecting(list_a, list_c) << endl;
}
