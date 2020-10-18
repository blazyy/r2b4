// Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to  a single stack (that is, pop() should return the same values as it would if there were just a single stack.)

// FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack.

#include <iostream>
#include <vector>
using namespace std;

// Solution
// Nothing to explain here. Pretty simple but kinda long.
// Time Complexity: O(n) - for pop_at(), due to left_shift(). Other operations are 0(1)
// Space Complexity - Not relevant.
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

    void left_shift(int stack, int index){
        while(stack < current_stack){
            for(int i = index; i < stacks[stack].size() - 1; i++)
                stacks[stack][i] = stacks[stack][i + 1];
            if(stack < current_stack) // This condition deals with shifting the first element of the next stack to the last element of the previous stack.
                stacks[stack][threshold - 1] = stacks[stack + 1][0];
            index = 0;
            stack++;
        }
        pop(); // Since we're left shifting, there is a duplicate element at the last, we just remove it using pop.
    }

    int pop_at(int stack, int index){
        if(stack > current_stack || stack < 0 || index >= threshold || index < 0){
            cout << "Invalid stack/element index!" << endl;
            return -1;
        }
        if(stack == current_stack){
            if(index >= stacks[stack].size()){
                cout << "Invalid stack/element index!" << endl;
                return -1;
            }
            else if(index == stacks[current_stack].size() - 1) return pop(); // If index to pop is last element, use pop() function.
        }
        int popped = stacks[stack][index];
        left_shift(stack, index);
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
    stack.print();
    cout << "Popping " << stack.pop_at(3, 3) << endl;
    stack.print();
}
