#include<iostream>
#include<string>
using namespace std;

class Stack{
    private:
        int size = 100;
        // items[size] is apparently illegal in C++ and legal in G++
        char * items = new char[size];
        int top = 0;
    public:
        void push(string item){
            if(!isFull())
                items[top++] = item;
            else
                cout << "Cannot add item, stack is full!" << endl;
        }
        string pop(){
            if(!isEmpty())
                return items[--top];
            return "";
        }
        string peek(){
            return items[top];
        }
        int get_size(){
            return top;
        }
        bool isEmpty(){
            return (top == 0) ? true : false;
        }
        bool isFull(){
            return (top == size) ? true : false;
        }
        void print_stack(){
            for(int i = 0; i < top; i++)
                cout << items[i] << " ";
            cout << endl;
        }
};

int main(void){
    Stack s;
    s.push("my");
    s.push("name");
    s.push("is");
    s.push("faaez");
    s.push("razeen");
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
}
