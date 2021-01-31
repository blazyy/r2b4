#include "helper.h"

// Given an array, cyclically rotate the array clockwise by one.

void solution(vector <int> &arr) {
    // Simple for loop solution
    // TC - O(n)
    // SC - O(1)
    int last = arr[arr.size() - 1]; // Saving this in a temporary variable since it gets overwritten
    for(int i = arr.size() - 1; i > 0; i--)
        arr[i] = arr[i - 1];
    arr[0] = last;
}

int main(void) {
    srand(time(NULL));
    vector <int> arr = generate_random_vector();
    print_array(arr);
    solution(arr);
    print_array(arr, false);
}
