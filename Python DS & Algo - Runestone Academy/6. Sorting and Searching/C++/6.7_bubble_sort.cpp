#include <iostream>
using namespace std;

void bubble_sort(int arr[], int size){
    bool swapped;
    for(int i = 0; i < size; i++){
        swapped = false;
        for(int j = 0; j < size - i - 1; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swapped = true;
            }
        }
        if(!swapped) return;
    }
}

void print_array(int arr[], int size){
    for(int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main(void){
    int size = 15;
    int * arr = new int[size];
    for(int i = 0; i < size; i++)
        arr[i] = rand() % 100;
    print_array(arr, size);
    bubble_sort(arr, size);
    print_array(arr, size);
}
