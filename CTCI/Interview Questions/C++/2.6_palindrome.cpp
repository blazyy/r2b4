// Implement a function to check if a linked list is a palindrome.

// Page 64

#include <iostream>
#include <vector>
using namespace std;

struct Node{
    char data;
    Node * next = NULL;
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
    void append(char data){
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
    void fill(vector <char> elements){
        if(head) head = NULL; // Doing this just to make the main function cleaner
        for(auto element : elements)
            append(element);
    }
    void fill(string str){
        vector <char> pal_vect (str.begin(), str.end());
        fill(pal_vect);
    }
    void print(){
        Node * current = head;
        while(current){
            cout << current -> data;
            current = current -> next;
        }
    }
    Node * get_head(){
        return head;
    }
    void set_head(Node * new_head){
        head = new_head;
    }
};

// Solution 1
// Using a stack store store the first half of the palindrome, then popping each and checking with latter half of linked list.
// Solution assumes that size of linked list is not known.
// Time Complexity: O(n), Space Complexity: O(n)
bool is_palindrome_1(LinkedList ll){
    Node * head = ll.get_head();
    // If string is less than 1 character long
    if(!head || !head -> next)
        return true;
    // If string is two characters long
    if(head -> data == head -> next -> data && !(head -> next -> next))
        return true;
    Node * slow = head;
    Node * fast = head;
    vector <char> stack;
    while(true){
        stack.push_back(slow -> data);
        slow = slow -> next;
        fast = fast -> next -> next;
        // If character has an odd number of characters
        if(!fast -> next){
            slow = slow -> next;
            break;
        }
        // If character has an even number of characters
        else if(fast -> next && !fast -> next -> next){
            stack.push_back(slow -> data);
            slow = slow -> next;
            break;
        }
    }
    while(slow){
        if(slow -> data != stack.back())
            return false;
        stack.pop_back();
        slow = slow -> next;
    }
    return true;
}

// I could've used a copy constructor but I'm still a noob in C++ so that didn't work out very well
LinkedList clone_ll(LinkedList ll){
    LinkedList rev_ll;
    Node * current = ll.get_head();
    while(current){
        Node * new_node = new Node;
        new_node -> data = current -> data;
        rev_ll.append(new_node);
        current = current -> next;
    }
    return rev_ll;
}

LinkedList reverse_and_clone_ll(LinkedList ll){
    LinkedList rev_ll = clone_ll(ll);
    Node * current = rev_ll.get_head();
    Node * prev = NULL;
    Node * next;
    while(current){
        next = current -> next;
        current -> next = prev;
        prev = current;
        current = next;
    }
    rev_ll.set_head(prev);
    return rev_ll;
}

bool compare_linked_lists(LinkedList ll, LinkedList rev_ll){
    Node * first = ll.get_head();
    Node * second = rev_ll.get_head();
    Node * fast = first;
    while(first && second){
        if(first -> data != second -> data) return false;
        first = first -> next;
        second = second -> next;
        if(fast -> next && fast -> next -> next)
            fast = fast -> next -> next;
        else break;
    }
    return true;
}

// Solution 2
// Reversing linked list and check first half of each list
// Time Complexity: O(n), Space Complexity: O(n)
bool is_palindrome_2(LinkedList ll){
    Node * head = ll.get_head();
    // If string is less than 1 character long
    if(!head || !head -> next)
        return true;
    // If string is two characters long
    if(head -> data == head -> next -> data && !(head -> next -> next))
        return true;
    LinkedList rev_ll = reverse_and_clone_ll(ll);
    return compare_linked_lists(ll, rev_ll);
}

int main(void){
    LinkedList ll;

    ll.fill("red rum sir is murder");
    ll.print();
    cout << " " << is_palindrome_1(ll);
    cout << " " << is_palindrome_2(ll) << endl;

    ll.fill("hello world lol");
    ll.print();
    cout << " " << is_palindrome_1(ll);
    cout << " " << is_palindrome_2(ll) << endl;

    ll.fill("i did did i");
    ll.print();
    cout << " " << is_palindrome_1(ll);
    cout << " " << is_palindrome_2(ll) << endl;

    ll.fill("dd");
    ll.print();
    cout << " " << is_palindrome_1(ll);
    cout << " " << is_palindrome_2(ll) << endl;
}

// Why did this reach 180 lines? Am I doing something wrong?
