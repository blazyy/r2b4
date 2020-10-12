// You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a funciton that adds the two numbers and returns the sum as a linked list.
// Input  (7 -> 1 -> 6) + (5 -> 9 -> 2) (That is, 617 + 295)
// Output 2 -> 1 -> 9 (That is, 912)

// Suppose the digits are stored in forward order. Repeat the above problem.
// Input  (6 -> 1 -> 7) + (2 -> 9 -> 5) (That is, 617 + 295)
// Output 9 -> 1 -> 2 (That is, 912)

// Page 64

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

void fill_linked_lists(int num1, int num2, LinkedList * list_a, LinkedList * list_b){
    while(num1){
        (*list_a).append(num1 % 10);
        num1 /= 10;
    }
    while(num2){
        (*list_b).append(num2 % 10);
        num2 /= 10;
    }
}

// Solution
// Since addition can also be done in reverse, just traverse the linked list while keeping in mind that there's a possibility of a carry.
// Time Complexity: O(n + m), Space Complexity(O(n + m)) where n and m are the number of digits in each number that's being added.
LinkedList * add_linked_lists_reverse(LinkedList * list_a, LinkedList * list_b){
    LinkedList * ll_sum = new LinkedList;
    int carry = 0, current_sum;
    Node * list_a_current = (*list_a).get_head();
    Node * list_b_current = (*list_b).get_head();
    while(list_a_current || list_b_current){
        current_sum = 0;
        if(list_a_current){
            current_sum += list_a_current -> data;
            list_a_current = list_a_current -> next;
        }
        if(list_b_current){
            current_sum += list_b_current -> data;
            list_b_current = list_b_current -> next;
        }
        current_sum += carry;
        if(current_sum >= 10){
            (*ll_sum).append(current_sum % 10);
            carry = 1;
        }
        else{
            (*ll_sum).append(current_sum);
            carry = 0;
        }
    }
    if(carry) (*ll_sum).append(carry);
    return ll_sum;
}

// Solution B
// I tried implementing this on my own but I got way too annoyed while trying to so I'm skipping this for now and I will kick myself in the future when I get asked this in an interview.

int main(void){
    srand(time(NULL)); // Using time as seed for RNG
    int num1 = rand() % 999999, num2 = rand() % 999999;
    LinkedList * list_a = new LinkedList;
    LinkedList * list_b = new LinkedList;
    fill_linked_lists(num1, num2, list_a, list_b);
    cout << num1 << " + " << num2 << " = " << num1 + num2 << endl;
    (*list_a).print();
    (*list_b).print();
    LinkedList * ll_sum = add_linked_lists_reverse(list_a, list_b);
    (*ll_sum).print();
}
