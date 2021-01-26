#include "helper.h"

// Write a program to find the maximum and minimum of an array using minimum number of comparisons

vector <int> solution_1(vector <int> &arr) {
    // Simple linear search.
    // TC - O(n)
    // SC - O(n)
    int minimum = INT_MAX;
    int maximum = INT_MIN;
    for(auto num : arr) {
        if(num < minimum)
            minimum = num;
        if(num > maximum)
            maximum = num;
    }
    return vector <int> {minimum, maximum};
}

vector <int> solution_2(vector <int> &arr) {
    // Compare in pairs. Still O(n), but comparisons decrease by a few numbers.
    // TC - O(n)
    // SC - O(n)
    int i, minimum, maximum, n = arr.size();
    if(n % 2 != 0) {
        minimum = maximum = arr[0];
        i = 1;
    }
    else {
        minimum = min(arr[0], arr[1]);
        maximum = max(arr[0], arr[1]);
        i = 2;
    }
    while(i < n - 1) {
        if(arr[i] > arr[i + 1]) {
            minimum = min(minimum, arr[i + 1]);
            maximum = max(maximum, arr[i]);
        }
        else {
            minimum = min(minimum, arr[i]);
            maximum = max(maximum, arr[i + 1]);
        }
        i += 2;
    }
    return vector <int> {minimum, maximum};
}

int main(void) {
    srand(time(NULL));
    vector <int> arr = generate_random_vector();
    vector <int> results_1 = solution_1(arr);
    vector <int> results_2 = solution_2(arr);
    print_array(arr);
    cout << endl << "Algo. 1 -> " << "Min: " << results_1[0] << " Max: " << results_1[1] << endl;
    cout << "Algo. 2 -> " << "Min: " << results_2[0] << " Max: " << results_2[1] << endl;
}
