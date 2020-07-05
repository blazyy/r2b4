#include <iostream>
#include <vector>
using namespace std;

bool binary_search(vector<int> arr, int ele, int start, int end){
    if(start > end)
        return false;
    int mid = (start + end) / 2;
    if(arr[mid] == ele)
        return true;
    else if(arr[mid] > ele)
        return binary_search(arr, ele, start, mid - 1);
    else
        return binary_search(arr, ele, mid + 1, end);
}

int main(void){
    vector <int> arr;
    for(int i = 1; i < 50; i+=2)
        arr.push_back(i);
    cout << binary_search(arr, 32, 0, arr.size());
}
