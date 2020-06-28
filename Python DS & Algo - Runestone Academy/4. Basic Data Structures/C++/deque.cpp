#include<iostream>
#include<string>
using namespace std;

class Deque{
    private:
        string items[50];
        int front = 0;
        int rear = 0;
    public:
        void addFront(string item){
            // Shifting all elements to right by 1
            for(int i = rear; i > front; i--)
                items[i] = items[i-1];
            items[front] = item;
            rear++;
        }
        void addRear(string item){
            items[rear++] = item;
        }
        string removeFront(){
            return items[front++];
        }
        string removeRear(){
            return items[--rear];
        }

        int size(){
            return rear-front;
        }
        bool isEmpty(){
            return (front == rear) ? true : false;
        }
        void printQueue(){
            for(int i = front; i < rear; i++)
                cout << items[i] << " ";
            cout << endl;
        }
        int getFront(){
            return front;
        }
        int getRear(){
            return rear;
        }
};

int main(void){
    Deque d;
    cout << d.isEmpty() << endl;
    d.addRear("4");
    d.addRear("dog");
    d.addFront("cat");
    d.addFront("true");
    cout << d.size() << endl;
    cout << d.isEmpty() << endl;
    d.addRear("8.4");
    cout << d.removeRear() << endl;
    cout << d.removeFront() << endl;
}
