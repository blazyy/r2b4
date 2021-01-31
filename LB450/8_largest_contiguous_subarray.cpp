#include "helper.h"

// Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

void solution_1(vector <int> &arr) {
    // Brute force solution, using a double for loop
    // TC - O(n^2)
    // SC - O(1)
    int start = 0, end = 0, highest = INT_MIN;
    for(int i = 0; i < arr.size(); i++) {
        int current_sum = 0;
        for(int j = i; j < arr.size(); j++) {
            current_sum += arr[j];
            if(current_sum > highest) {
                highest = current_sum;
                start = i;
                end = j;
            }
        }
    }
    cout << endl << "Maximum sum is " << highest << ", from index " << start << " to " << end << endl;
}

void solution_2(vector <int> &arr) {
    // Kadane's Algorithm
    // TC - O(n)
    // SC - O(1)
    int current_sum, max_sum, start, end;
    current_sum = max_sum = arr[0];
    for(int i = 1; i < arr.size(); i++) {
        current_sum = max(arr[i], arr[i] + current_sum); // If this doesn't make sense, remember that the array contains negative numbers
        max_sum = max(max_sum, current_sum);
    }
    cout << "Maximum sum is " << max_sum << endl;
}

int main(void) {
    srand(time(NULL));
    vector <int> arr = generate_random_vector(10, 100, true);
    print_array(arr);
    solution_1(arr);
    solution_2(arr);
}
