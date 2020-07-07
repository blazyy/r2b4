#include <iostream>
using namespace std;

void selection_sort(int * arr, int size){
    int max_idx, last_idx;
    for(int i = 0; i < size; i++){
        last_idx = size - i - 1;
        max_idx = 0;
        for(int j = 0; j < last_idx+1; j++){
            if(arr[j] > arr[max_idx])
                max_idx = j;
        }
        swap(arr[max_idx], arr[last_idx]);
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
        arr[i] = rand() % 100;
    print_array(arr, size);
    selection_sort(arr, size);
    print_array(arr, size);
}
