// This header file contains important functions that I will mostly use for printing to the console.
// This is in a header file because I don't want to clutter my code.

#ifndef HELPER_H // To make sure you don't declare the function more than once by including the header multiple times.
#define HELPER_H

#include <iostream>
#include <algorithm>
#include <vector>
#include <ctime>
#include <vector>
#include <queue>

using namespace std;

vector <int> generate_random_vector(int size=10) {
    vector <int> vect;
    for(int i = 0; i < size; i++)
        vect.push_back(rand() % 100);
    return vect;
}

void print_array(vector <int> &arr, bool new_line=true) {
    if(new_line) cout << endl;
    for(auto num : arr)
        cout << num << " ";
    cout << endl;
}

#endif
