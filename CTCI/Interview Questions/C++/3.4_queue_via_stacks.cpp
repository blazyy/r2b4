// Implement a MyQueue class which implements a queue using two stacks.

#include <iostream>
#include <stack>
using namespace std;

// Solution
// Using a default Python list as our stack
// Remember that pushing items into and popping them out of a stack reverses their order. Do this again, and the order stays the same. This is what we want, since a queue operates on the FIFO basis.
// Time Complexity: O(1) for enqueue, O(n) for dequeue
// Space Complexity: O(n)? Due to extra stack?
class MyQueue{
private:
    stack <int> inbox;
    stack <int> outbox;
public:
    void enqueue(int item){
        inbox.push(item);
    }
    int dequeue(){
        if(outbox.size() == 0){
            if(inbox.size() == 0){
                cout << "Cannot dequeue from empty queue!" << endl;
                return -1;
            }
            while(inbox.size() != 0){
                outbox.push(inbox.top());
                inbox.pop();
            }
        }
        int popped = outbox.top();
        outbox.pop();
        return popped;
    }
};

int main(void){
    MyQueue queue;
    queue.enqueue(1); queue.enqueue(2); queue.enqueue(3); queue.enqueue(4); queue.enqueue(5);
    cout << queue.dequeue() << endl;
    cout << queue.dequeue() << endl;
    cout << queue.dequeue() << endl;
    cout << queue.dequeue() << endl;
    cout << queue.dequeue() << endl;
}
