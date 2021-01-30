// This header file contains important functions that I will mostly use for printing to the console.
// This is in a header file because I don't want to clutter my code.

#ifndef HELPER_H // To make sure you don't declare the function more than once by including the header multiple times.
#define HELPER_H

#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#include <ctime>
#include <vector>
#include <queue>

using namespace std;

vector <int> generate_random_vector(int size=10, int upper_bound=100, bool include_negative=false) {
    vector <int> vect;
    for(int i = 0; i < size; i++) {
        if(include_negative)
            vect.push_back((rand() % upper_bound) - (upper_bound / 2));
        else
            vect.push_back(rand() % upper_bound);
    }
    return vect;
}

vector <int> generate_distinct_random_vector(int size=10, int upper_bound=100) {
    if(size > upper_bound) {
        cout << "Upper bound of number generation too small for given size!" << endl;
        exit(0);
    }
    vector <int> vect;
    int i = 0;
    while(i < size) {
        int rand_num = rand() % 100;
        if(find(vect.begin(), vect.end(), rand_num) != vect.end()) continue;
        else {
            vect.push_back(rand_num);
            i++;
        }
    }
    return vect;
}



void print_array(vector <int> &arr, bool new_line=true) {
    if(new_line) cout << endl;
    for(auto num : arr)
        cout << num << " ";
    cout << endl;
}

void shuffle_array(vector <int> &arr) {
    unsigned seed = 0;
    int n = sizeof(arr) / sizeof(arr[0]);
    shuffle(arr.begin(), arr.end(), default_random_engine(seed));
}

#endif
