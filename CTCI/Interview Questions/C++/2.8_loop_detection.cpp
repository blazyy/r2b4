// Give a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

// DEFINITION
// Circular linked listL A (corrput) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

// EXAMPLE
// Input  A - > B -> C -> D - > E -> C [the same C as earlier]
// Output C

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
    Node * get_head(){
        return head;
    }
};

// Solution
// Floyd's tortoise and hare
// Time Complexity: O(n)
// Space Complexity: O(1)
bool has_loop(LinkedList ll){
    Node * slow = ll.get_head();
    Node * fast = ll.get_head();
    bool loop_exists = false;
    while(slow && fast){
        slow = slow -> next;
        if(fast -> next)
            fast = fast -> next -> next; // This is for when the linked list doesn't have a loop
        if(fast == slow){
            fast = ll.get_head();
            while(true){
                if(fast == slow){
                    cout << fast -> data << endl;
                    return true;
                }
                fast = fast -> next;
                slow = slow -> next;
            }
        }
    }
    return loop_exists;
}


// Replicating the following
// 1 -> 2 -> 3
//         /  \
//       5 <-- 4

int main(void){
    LinkedList ll;
    Node * node1 = new Node(1);
    Node * node2 = new Node(2);
    Node * repeated_node = new Node(3);
    Node * node4 = new Node(4);
    Node * node5 = new Node(5);
    ll.append(node1);
    ll.append(node2);
    ll.append(repeated_node);
    ll.append(node4);
    ll.append(node5);
    ll.append(repeated_node);
    cout << has_loop(ll) << endl;

    LinkedList another_ll;
    Node * node6 = new Node(1);
    Node * node7= new Node(2);
    Node * node8 = new Node(4);
    Node * node9 = new Node(5);
    another_ll.append(node6);
    another_ll.append(node7);
    another_ll.append(node8);
    another_ll.append(node9);
    cout << has_loop(another_ll) << endl;
}
