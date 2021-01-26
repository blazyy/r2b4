#include "helper.h"

// Write a program to reverse an array.

void solution_1(vector <int> &arr){
    int start = 0, end = arr.size() - 1;
    while(start < end) {
        swap(arr[start++], arr[end--]);
    }
}

int main(void) {
    srand(time(NULL));
    vector <int> arr = generate_random_vector();
    print_array(arr);
    solution_1(arr);
    print_array(arr);
}
