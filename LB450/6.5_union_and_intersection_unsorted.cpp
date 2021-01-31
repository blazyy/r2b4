#include "helper.h"

// Given two arrays A and B of size N and M respectively. The task is to find union and intersection between these two arrays.
// Assumption: All values in the array are unique.

void solution_1(vector <int> &a, vector <int> &b) {
    // A cheaty way using sets. Not really what the question asked for.
    set <int> union_set;
    set <int> intersection_set;
    for(auto num : a) union_set.insert(num);
    for(auto num : b)
        if(union_set.find(num) != union_set.end())
            intersection_set.insert(num);
    for(auto num : b)
        union_set.insert(num); // Cannot add this line to the for loop above, since elements in array B will be considered as elements of array A

    cout << endl << "Union: \t\t"; print_set(union_set);
    cout << "Intersection: \t"; print_set(intersection_set);
    cout << endl;
}

void solution_2(vector <int> &a, vector <int> &b) {
    // Simple iterative solution
    // TC - O(m x n) where m and n are the size of the arrays
    // SC - O(1)
    vector <int> union_vect;
    vector <int> intersection_vect;
    for(auto num : a) {
        union_vect.push_back(num);
        if(find(b.begin(), b.end(), num) != b.end())
            intersection_vect.push_back(num);
    }
    for(auto num : b) {
        if(find(union_vect.begin(), union_vect.end(), num) == union_vect.end())
            union_vect.push_back(num);
    }
    cout << "Union: \t\t"; for(auto num : union_vect) cout << num << " "; cout << endl;
    cout << "Intersection: \t"; for(auto num : intersection_vect) cout << num << " "; cout << endl;
    cout << endl;
}

void solution_3(vector <int> &a, vector <int> &b) {
    // Use a hash-set to store all values in first array. In C++, unordered_set has average TC as O(1) and worst case TC as O(n)
    // TC - O(m + n)
    // SC - O(m) or O(n)
    vector <int> union_vect;
    vector <int> intersection_vect;
    unordered_set <int> s;
    for(auto num : a) {
        union_vect.push_back(num);
        s.insert(num);
    }
    for(auto num : b) {
        if(s.find(num) != s.end())
            intersection_vect.push_back(num);
        else
            union_vect.push_back(num);
    }
    cout << "Union: \t\t"; for(auto num : union_vect) cout << num << " "; cout << endl;
    cout << "Intersection: \t"; for(auto num : intersection_vect) cout << num << " "; cout << endl;
    cout << endl;
}

int main(void) {
    srand(time(NULL));
    vector <int> a = generate_distinct_random_vector(10);
    vector <int> b = generate_distinct_random_vector(10);
    print_array(a);
    print_array(b, false);

    solution_1(a, b);
    solution_2(a, b);
    solution_3(a, b);
}
