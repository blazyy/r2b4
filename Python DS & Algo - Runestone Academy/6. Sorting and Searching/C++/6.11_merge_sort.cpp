#include <iostream>
using namespace std;

void merge(int * left, int lsize, int * right, int rsize, int * arr, int size){
    int l_idx = 0, r_idx = 0, idx = 0;
    while(l_idx < lsize && r_idx < rsize)
        if(left[l_idx] <= right[r_idx])
            arr[idx++] = left[l_idx++];
        else
            arr[idx++] = right[r_idx++];
    while(l_idx < lsize)
        arr[idx++] = left[l_idx++];
    while(r_idx < rsize)
        arr[idx++] = right[r_idx++];
}


void merge_sort(int * arr, int size){
    if(size < 2) return;
    int mid = size/2, lsize = mid, rsize = size - mid;
    int * left = new int[lsize];
    int * right = new int[rsize];
    for(int i = 0; i < mid; i++)
        left[i] = arr[i];
    for(int i = mid; i < size; i++)
        right[i - mid] = arr[i];
    merge_sort(left, lsize);
    merge_sort(right, rsize);
    merge(left, lsize, right, rsize, arr, size);
}

void print_array(int * arr, int size){
    for(int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main(void){
    int size = 10;
    int * arr = new int[size];
    for(int i = 0; i < size; i++)
        arr[i] = rand() % 100;
    print_array(arr, size);
    merge_sort(arr, size);
    print_array(arr, size);
}
