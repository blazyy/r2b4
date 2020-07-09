#include <iostream>
#include <time.h>
using namespace std;

void bubble_sort(int * arr, int size){
    for(int i = 0; i < size; i++)
        for(int j = 0; j < size - i - 1; j++)
            if(arr[j] >= arr[j+1])
                swap(arr[j], arr[j+1]);
}

void selection_sort(int * arr, int size){
    int min_idx;
    for(int i = 0; i < size; i++){
        min_idx = i;
        for(int j = i; j < size; j++)
            if(arr[j] < arr[min_idx])
                min_idx = j;
        swap(arr[min_idx], arr[i]);
    }
}

void insertion_sort(int * arr, int size){
    int current, value;
    for(int i = 1; i < size; i++){
        current = i;
        value = arr[current];
        while(current > 0 && arr[current-1] > value){
            arr[current] = arr[current-1];
            current--;
        }
        arr[current] = value;
    }
}

void merge_sort(int * arr, int size){
    if(size < 2)
        return;
    int mid = size / 2, lsize = mid, rsize = size - mid;
    int * left = new int[lsize];
    int * right = new int[rsize];
    for(int i = 0; i < mid; i++)
        left[i] = arr[i];
    for(int i = mid; i < size; i++)
        right[i-mid] = arr[i];
    merge_sort(left, lsize);
    merge_sort(right, rsize);
    int l_idx = 0, r_idx = 0, idx = 0;
    while(l_idx < lsize && r_idx < rsize){
        if(left[l_idx] <= right[r_idx])
            arr[idx++] = left[l_idx++];
        else
            arr[idx++] = right[r_idx++];
    }
    while(l_idx < lsize)
        arr[idx++] = left[l_idx++];
    while(r_idx < rsize)
        arr[idx++] = right[r_idx++];
}

int partition(int * arr, int start, int end){
    int pivot_value = arr[end], pivot_index = end;
    int p_index = start;
    for(int i = start; i < end; i++)
        if(arr[i] <= pivot_value)
            swap(arr[i], arr[p_index++]);
    swap(arr[pivot_index], arr[p_index]);
    return p_index;
}

void quick_sort(int * arr, int start, int end){
    if(start < end){
        int p_index = partition(arr, start, end);
        quick_sort(arr, start, p_index - 1);
        quick_sort(arr, p_index + 1, end);
    }
}

void print_array(int * arr, int size){
    for(int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main(void){
    srand(time(NULL));
    int size = 10;
    int * arr = new int[size];
    for(int i = 0; i < size; i++)
        arr[i] = rand() % 100;
    print_array(arr, size);
    quick_sort(arr, 0, size);
    print_array(arr, size);
}
