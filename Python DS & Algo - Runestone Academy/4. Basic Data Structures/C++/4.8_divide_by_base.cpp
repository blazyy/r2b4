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
        void push(char item){
            if(!isFull())
                items[top++] = item;
            else
                cout << "Cannot add item, stack is full!" << endl;
        }
        char pop(){
            if(!isEmpty())
                return items[--top];
            return ' ';
        }
        char peek(){
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

string divide_by_base(int num, int base){
    Stack stack;
    char digits[] = "0123456789ABCDEF";
    char base_num[10];
    int rem, base_num_idx = 0;
    while(num){
        rem = num % base;
        stack.push(digits[rem]);
        num = num / base;
    }
    while(!stack.isEmpty())
        base_num[base_num_idx++] = stack.pop();
    base_num[base_num_idx] = '\0';
    return base_num;
}

int main(void){
    cout << divide_by_base(25, 2) << endl; // 11001
    cout << divide_by_base(256, 16) << endl;  // 100
    cout << divide_by_base(25, 8) << endl; // 31
    cout << divide_by_base(233, 8) <<endl;  // 351
    cout << divide_by_base(233, 16) <<endl;  // E9
}
