#include<iostream>
using namespace std;

int recursive_array_sum(int arr[], int index){
    if(index == 0)
        return arr[index];
    return arr[index] + recursive_array_sum(arr, index - 1);
}

int main(void){
    int size = 10;
    int * arr = new int[size];
    for(int i = 0; i < size; i++)
        arr[i] = i;
    cout << recursive_array_sum(arr, size - 1) << endl;
}
