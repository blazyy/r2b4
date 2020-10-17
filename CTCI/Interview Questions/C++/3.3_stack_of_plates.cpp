// Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to  a single stack (that is, pop() should return the same values as it would if there were just a single stack.)

// FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack.

#include <iostream>
#include <vector>
using namespace std;

class SetOfStacks{
private:
    int threshold;
    int current_stack = 0;
    vector <vector<int>> stacks;
public:
    SetOfStacks(int thresh){
        threshold = thresh;
        vector <int> initial_vector;
        stacks.push_back(initial_vector);
    }
    void push(int item){
        if(stacks[current_stack].size() == threshold){
            vector <int> new_vect = {};
            stacks.push_back(new_vect);
            current_stack++;
        }
        stacks[current_stack].push_back(item);
    }
    int pop(){
        if(current_stack == 0 && stacks[current_stack].size() == 0){
            cout << "Cannot pop from empty list! ";
            return -1;
        }
        int popped;
        if(stacks[current_stack].size() == 0){
            stacks.pop_back();
            current_stack--;
        }
        popped = stacks[current_stack].back();
        stacks[current_stack].pop_back();
        return popped;
    }
    void print(){
        for(int i = 0; i <= current_stack; i++){
            for(int j = 0; j < threshold; j++)
                if(j < stacks[i].size())
                    cout << stacks[i][j] << " ";
            cout << "- ";
        }
        cout << endl;
    }
};

void print_vector(vector <int> vect){
    for(int i = 0; i < vect.size(); i++)
        cout << vect[i] << " ";
    cout << endl;
}

vector <int> create_random_vect(int num_elements){
    vector <int> rand_vect;
    for(int i = 0; i < num_elements; i++)
        rand_vect.push_back(rand() % 100);
    return rand_vect;
}

int main(void){
    int num_elements = 27;
    vector <int> rand_vect = create_random_vect(num_elements);
    SetOfStacks stack(5);
    for(auto num : rand_vect) stack.push(num);
    print_vector(rand_vect);
    cout << "Stack before popping: "; stack.print();
    for(int i = 0; i < 10; i++) cout << stack.pop() << endl;
    cout << "Stack after popping: "; stack.print();
}
