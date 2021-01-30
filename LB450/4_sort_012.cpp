#include "helper.h"

// Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

void solution_1(vector <int> &arr) {
    // Brute force. Count number of 0s, 1s, and 2s, and replace the values in the original array with these values.
    // TC - O(n)
    // SC - O(1)
    vector <int> vect;
    int i, num_zeroes, num_ones, num_twos;
    i = num_zeroes = num_ones = num_twos = 0;
    while(i < arr.size()) {
        if(arr[i] == 0) num_zeroes++;
        else if(arr[i] == 1) num_ones++;
        else num_twos++;
        i++;
    }
    i = 0;
    while(num_zeroes--) arr[i++] = 0;
    while(num_ones--) arr[i++] = 1;
    while(num_twos--) arr[i++] = 2;
}

void solution_2(vector <int> &arr) {
    // Using three pointers. Elements from index 0 to start - 1 always have zeroes. From start to mid - 1 there are only ones. From mid to high - 1, there are unknowns. And from high to n-1, there are 2s.
    // TC - O(n)
    // SC - O(1)
    int start = 0, index = 0, end = arr.size() - 1;
    while(index <= end) {
        if(arr[index] == 0) swap(arr[start++], arr[index++]);
        else if(arr[index] == 1) index++; // Only incrementing index here because start index doesn't know if there are any upcoming zeros.
        else swap(arr[index], arr[end--]);
    }
}

int main(void) {
    srand(time(NULL));
    vector <int> arr = generate_random_vector(10, 3);
    print_array(arr);
    solution_1(arr);
    print_array(arr, false); shuffle_array(arr);
    solution_2(arr);
    print_array(arr, false);
}
