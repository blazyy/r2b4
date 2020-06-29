#include <iostream>
using namespace std;

struct Node{
    int data;
    struct Node * next = NULL;
};

class LinkedList{
protected:
    struct Node * head = NULL;
    unsigned int size = 0;
public:
    bool isEmpty(){
        return (head == NULL) ? true : false;
    }
    int get_size(){
        return size;
    }
    void append(int data){
        struct Node * current = head;
        struct Node * newNode = new Node;
        newNode -> data = data;
        if(head == NULL) head = newNode;
        else{
            while(current -> next)
                current = current -> next;
            current -> next = newNode;
        }
        size += 1;
    }
    int index(int ele){
        struct Node * current = head;
        int index = 0;
        while(current){
            if(current -> data == ele)
                return index;
            index += 1;
            current = current -> next;
        }
        return -1;
    }
    int pop(int index_to_pop){
        int popped_num, index = 0;
        if(index_to_pop == 0){
            popped_num = head -> data;
            head = head -> next;
        }
        else if(index_to_pop >= size || index_to_pop < 0){
            cout << "Cannot pop! Index cannot be negative or greater than or equal to the size of the list! ";
            return -1;
        }
        else if(index_to_pop == size - 1){
            struct Node * current = head;
            while(current -> next -> next) current = current -> next;
            popped_num = current -> next -> data;
            current -> next = NULL;
        }
        else if(index_to_pop < size){
            struct Node * current = head;
            struct Node * prev = head;
            while(current -> next){
                if(index == index_to_pop){
                    popped_num = current -> data;
                    prev -> next = current -> next;
                }
                index += 1;
                prev = current;
                current = current -> next;
            }
        }
        size -= 1;
        return popped_num;
    }
    void insert(int data, int index_to_insert){
        int index = 0;
        if(head == NULL){
            cout << "Cannot insert to an empty list! Use append." << endl;
            return;
        }
        if(index_to_insert < 0 || index_to_insert > size)
            cout << "Cannot insert! Index to insert cannot be negative or greater than or equal to the size of the list! " << endl;
        else{
            struct Node * newNode = new Node;
            newNode -> data = data;
            if(index_to_insert == 0){
                newNode -> next = head;
                head = newNode;
            }
            else if(index_to_insert == size){
                struct Node * current = head;
                while(current -> next)
                    current = current -> next;
                current -> next = newNode;
            }
            else{
                struct Node * current = head;
                struct Node * prev = head;
                while(current){
                    if(index == index_to_insert){
                        prev -> next = newNode;
                        newNode -> next = current;
                        break;
                    }
                    index += 1;
                    prev = current;
                    current = current -> next;
                }
            }
            size += 1;
        }
    }
    void remove(int ele){
        if(head -> data == ele)
            head = head -> next;
        else{
            struct Node * current = head;
            struct Node * prev = head -> next;
            while(current){
                if(current -> data == ele)
                    prev -> next = current -> next;
                prev = current;
                current = current -> next;
            }
        }
        size -= 1;
    }
    int search(int ele){
        int found_index = -1, index = 1;
        if(head -> data == ele)
            found_index = 0;
        else{
            struct Node * current = head -> next;
            while(current){
                if(current -> data == ele)
                    found_index = index;
                index += 1;
                current = current -> next;
            }
        }
        return found_index;
    }
    void slice(int start_index, int end_index){
        if(start_index < 0 || end_index >= size || start_index == end_index){
            cout << "Improper indices. Returning." << endl;
        }
        else{
            int index = 0;
            struct Node * current = head;
            while(current){
                if(index >= start_index && index < end_index)
                    cout << current -> data << " ";
                    if(index >= end_index) break;
                index += 1;
                current = current -> next;
            }
            cout << endl;
        }
    }
    void print(){
        struct Node * current = head;
        while(current){
            cout << current -> data << " ";
            current = current -> next;
        }
        cout << endl;
    }
};

class OrderedList : public LinkedList{
public:
    void insert(int data){
        cout << "Cannot insert to an index in an ordered list!" << endl;
    }
    void append(int data){
        cout << "Cannot append to an ordered list!" << endl;
    }
    void add(int data){
        struct Node * newNode = new Node;
        newNode -> data = data;
        if(head == NULL)
            head = newNode;
        else{
            if(data <= head -> data){
                newNode -> next = head;
                head = newNode;
            }
            else{
                struct Node * current = head;
                struct Node * prev = head;
                while(current && current -> data < data){
                    prev = current;
                    current = current -> next;
                }
                prev -> next = newNode;
                newNode -> next = current;
            }
        }
    }
};

int main(void){
    OrderedList ol;
    LinkedList ll;
}
