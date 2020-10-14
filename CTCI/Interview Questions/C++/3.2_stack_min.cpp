// How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
// Page 67

#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

// Solution
// Using two stacks. One, for storing elements and the other to store the minimums. Only add to the minimum stack when the initial stack is empty or the new item that is being added is smaller than the current minimum (which is at the top of the minimum stack)
// Time Complexity: O(1) for all operations
// Space Complexity: O(n) (This only happens if you fill the stack with elements in descending order)
class Stack{
private:
    vector <int> items;
    vector <int> mins; // This contains only the new minimums, i.e. numbers that are smaller than the current minimum.
public:
    void push(int item){
        if(items.size() == 0 || item < mins.back())
            mins.push_back(item);
        items.push_back(item);
    }

    int pop(){
        int popped;
        if(items.size() == 0) return -1;
        if(items.back() == mins.back())
            mins.pop_back();
        popped = items.back();
        items.pop_back();
        return popped;
    }

    int get_min(){
        return mins.back();
    }
};

vector <int> create_random_vect(int num_elements){
    vector <int> return_vect;
    for(int i = 0; i < num_elements; i++)
        return_vect.push_back(rand() % 100);
    return return_vect;
}

void print_vect(vector <int> vect){
    for(int i = 0; i < vect.size(); i++)
        cout << vect[i] << " ";
    cout << endl;
}


int main(void){
    srand(time(NULL)); // Using time as seed for RNG
    Stack stack;
    int num_elements = 10;
    vector <int> random_vect = create_random_vect(num_elements);
    print_vect(random_vect);
    for(auto number : random_vect)
        stack.push(number);
    for(int i = 0; i < num_elements; i++){
        cout << stack.get_min() << " ";
        stack.pop();
    }
}
