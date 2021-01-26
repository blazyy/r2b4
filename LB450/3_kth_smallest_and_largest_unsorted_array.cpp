#include "helper.h"

//  Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest and largest element in the given array.
// It is given that all array elements are distinct.

vector <int> solution_1(vector <int> &arr, int k) {
    // Sort and scan.
    // TC - O(n log n)
    // SC - O(1)
    sort(arr.begin(), arr.end());
    return vector <int> {arr[k - 1], arr[arr.size() - k]};
}

vector <int> solution_2(vector <int> &arr, int k) {
    // Use a priority queue.
    // TC - O(n + (k * log n))
    // SC - O(n)
    int minimum, maximum;
    priority_queue <int, vector<int>, greater<int>> min_heap;
    priority_queue <int> max_heap;
    for(auto num : arr) {
        min_heap.push(num);
        max_heap.push(num);
    }
    while(--k) {
        min_heap.pop();
        max_heap.pop();
    }
    return vector <int> {min_heap.top(), max_heap.top()};
}

int main(void) {
    srand(time(NULL));
    int size = 10;
    vector <int> arr = generate_random_vector(size);
    int k = (rand() % (size - 1)) + 1; // Random k betwqeen 0 and 1
    print_array(arr);
    vector <int> result_1 = solution_1(arr, k);
    vector <int> result_2 = solution_2(arr, k);
    print_array(arr, false);
    cout << endl << "k = " << k << endl;
    cout << endl << "Algo. 1" << endl << "Min: " << result_1[0] << endl << "Max: " << result_1[1] << endl;
    cout << endl << "Algo. 2" << endl << "Min: " << result_2[0] << endl << "Max: " << result_2[1] << endl;
}
