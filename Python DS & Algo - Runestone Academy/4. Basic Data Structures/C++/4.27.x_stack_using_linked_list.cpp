#include <iostream>
using namespace std;

struct Node{
    int data;
    struct Node * next = NULL;
    struct Node * prev = NULL;
};

class Stack{
private:
    struct Node * top = NULL;
public:
    void push(int data){
        struct Node * newNode = new Node;
        newNode -> data = data;
        if(top == NULL)
            top = newNode;
        else{
            newNode -> prev = top;
            top = newNode;
        }
    }
    int pop(){
        int return_num;
        if(top == NULL)
            return -1;
        else{
            return_num = top -> data;
            top = top -> prev;
            top -> next = NULL;
        }
        return return_num;
    }
    void display(){
        cout << "Top -> ";
        struct Node * current = top;
        while(current != NULL){
            cout << current -> data << " ";
            current = current -> prev;
        }
        cout << "<- Bottom" << endl;
        free(current);
    }
};

int main(void){
    Stack s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.push(5);
    s.display();
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    s.push(3);
    s.push(5);
    s.push(7);
    s.push(9);
    s.pop();
    s.display();
}
