#include<iostream>
using namespace std;

struct Node{
    int data;
    struct Node * next = NULL;
};

class Queue{
private:
    struct Node * front = NULL;
    struct Node * rear = NULL;
public:
    void enqueue(int data){
        struct Node * newNode = new Node;
        newNode -> data = data;
        if(front == NULL)
            front = rear = newNode;
        else{
            rear -> next = newNode;
            rear = rear -> next;
        }
    }

    int dequeue(){
        if(front == NULL)
            return -1;
        else{
            int return_num = front -> data;
            front = front -> next;
            return return_num;
        }
    }

    void display(){
        cout << "F -> ";
        Node * current = front;
        while(current){
            cout << current -> data << " ";
            current = current -> next;
        }
        cout << "<- R " << endl;
    }
};

int main(void){
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.dequeue();
    q.dequeue();
    q.enqueue(4);
    q.enqueue(5);
    q.display();
}
