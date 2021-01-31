#include "helper.h"

// Given two SORTED arrays A and B of size N and M respectively. The task is to find union and intersection between these two arrays.

void solution(vector <int> &a, vector <int> &b) {
    // Simple linear scan using two pointers. Kinda like merge sort.
    // TC - O(m + n)
    // SC - O(1)
    vector <int> union_vect;
    vector <int> intersection_vect;
    int a_idx = 0, b_idx = 0;

    while(a_idx < a.size() and b_idx < b.size()) {
        while((a_idx < a.size() - 1) and (a[a_idx] == a[a_idx + 1])) // Handles duplicate elements. Just moves pointer forward until the element after it is not a duplicate
            a_idx++;
        while((b_idx < b.size() - 1) and (b[b_idx] == b[b_idx + 1]))
            b_idx++;
        if(a[a_idx] == b[b_idx]) {
            intersection_vect.push_back(a[a_idx]);
            union_vect.push_back(a[a_idx]);
            a_idx++;
            b_idx++;
        }
        else if(a[a_idx] < b[b_idx])
            union_vect.push_back(a[a_idx++]);
        else
            union_vect.push_back(b[b_idx++]);
    }
    while(a_idx < a.size())
        union_vect.push_back(a[a_idx++]);
    while(b_idx < a.size())
        union_vect.push_back(b[b_idx++]);

    cout << endl;
    cout << "Union: \t\t"; for(auto num : union_vect) cout << num << " "; cout << endl;
    cout << "Intersection: \t"; for(auto num : intersection_vect) cout << num << " "; cout << endl;
    cout << endl;
}

int main(void) {
    srand(time(NULL));
    vector <int> a = generate_random_vector(10, 30); sort(a.begin(), a.end());
    vector <int> b = generate_random_vector(10, 30); sort(b.begin(), b.end());
    print_array(a);
    print_array(b, false);
    solution(a, b);
}
