#include <iostream>
using namespace std;

int partition(int * arr, int start, int end){
    int pivot = arr[end];
    int p_index = start;
    for(int i = start; i < end; i++)
        if(arr[i] <= pivot)
            swap(arr[i], arr[p_index++]);
    swap(arr[end], arr[p_index]);
    return p_index;
}

void quick_sort(int * arr, int start, int end){
    // The condition below doesn't get satisfied if there's only one element to the left or right of partition index
    // In which case, start >= end, which means we'll have to return
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
    int size = 10;
    int * arr = new int[size];
    for(int i = 0; i < size; i++)
        arr[i] = rand() % 10;
    print_array(arr, size);
    quick_sort(arr, 0, size);
    print_array(arr, size);
}
