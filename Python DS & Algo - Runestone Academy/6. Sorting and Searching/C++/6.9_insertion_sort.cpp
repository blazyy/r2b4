#include <iostream>
using namespace std;

void insertion_sort(int * arr, int size){
    int current, value;
    for(int i = 1; i < size; i++){
        current = i;
        value = arr[i];
        // when current == 0, there will be no more elements to shift
        while(current > 0 && arr[current-1] > value){
            arr[current] = arr[current-1];
            current = current - 1;
        }
        arr[current] = value;
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
    insertion_sort(arr, size);
    print_array(arr, size);
}
