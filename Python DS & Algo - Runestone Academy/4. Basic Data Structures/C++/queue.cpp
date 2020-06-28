#include<iostream>
#include<string>
using namespace std;

class Queue{
    private:
        int size = 100, front = 0, rear = 0;
        string * queue = new string[size];
    public:
        void enqueue(string item){
            if(!isFull())
                queue[++rear] = item;
            else
                cout << "Cannot enqueue, queue is full!" << endl;
        }
        string dequeue(){
            if(!isEmpty())
                return queue[++front];
            return "";
        }
        int get_size(){
            return rear-front;
        }
        bool isEmpty(){
            return (front == rear) ? true : false;
        }
        bool isFull(){
            return (rear >= size) ? true : false;
        }
};

int main(void){
    Queue q;
    cout << q.isEmpty() << endl;
    q.enqueue("4");
    q.enqueue("dog");
    q.enqueue("true");
    cout << q.get_size() << endl;
    cout << q.isEmpty() << endl;
    q.enqueue("8.4");
    cout << q.dequeue() << endl;
    cout << q.dequeue() << endl;
    cout << q.get_size() << endl;
}
