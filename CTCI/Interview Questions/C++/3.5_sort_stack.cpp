// Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may NOT copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
// Page 67

#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

// Solution
// The buffer stack will always be sorted when building it. Taking the current element (most recently popped from original stack), pop all elements greater than it from the buffer to the original stack (yes, the original stack), and then put the element into the buffer. My explanation is pretty bad lol so if the future me is confused just refer back to the book.
// Time Complexity: O(n^2)
// Space Complexity: Doesn't make sense to mention here but it's O(n)

class Stack{
private:
    vector <int> items;
public:
    void push(int item){
        items.push_back(item);
    }
    int pop(){
        int popped = items.back();
        items.pop_back();
        return popped;
    }
    int peek(){
        return items.back();
    }
    bool is_empty(){
        return items.size() == 0;
    }
    void sort_stack(){
        if(is_empty()) return;
        int current, temp;
        vector <int> buffer;
        while(items.size() > 0){
            current = items.back();
            items.pop_back();
            while(buffer.size() > 0 && buffer.back() > current){
                temp = buffer.back();
                buffer.pop_back();
                push(temp);
            }
            buffer.push_back(current);
        }
        while(buffer.size() > 0){
            temp = buffer.back();
            buffer.pop_back();
            push(temp);
        }
    }
    void print_stack(){
        for(auto item : items)
            cout << item << " ";
        cout << endl;
    }
};

vector <int> gen_rand_array(int size){
    vector <int> elements;
    for(int i = 0; i < size; i++)
        elements.push_back(rand() % 100);
    return elements;
}

int main(void){
    srand(time(NULL));
    Stack s;
    vector <int> elements = gen_rand_array(10);
    for(auto element : elements) s.push(element);
    s.print_stack();
    s.sort_stack();
    s.print_stack();
}
