#include "helper.h"

// Move all negative numbers to beginning and positive to end with constant extra space. Note: Order is not important here.

void solution(vector <int> &arr) {
    // Simple two pointer solution
    // TC - O(n)
    // SC - O(1)
    int neg_index = 0, index = 0;
    while(index < arr.size()) {
        if(arr[index] < 0)
            swap(arr[index], arr[neg_index++]);
        index++;
    }
}

int main(void) {
    srand(time(NULL));
    vector <int> arr = generate_random_vector(10, 100, true);
    print_array(arr);
    solution(arr);
    print_array(arr, false);
}
