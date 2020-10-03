#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class BinaryHeap{
private:
    vector <int> heap {0};
    int size = 0;
public:
    void insert(int item){
        heap.push_back(item);
        size++;
        perc_up(size);
    }
    void perc_up(int idx){
         while(idx / 2 > 0){
             int parent_idx = idx / 2;
             if(heap[idx] < heap[parent_idx]){
                 swap(heap[idx], heap[parent_idx]);
                 idx /= 2;
             }
             else break;
         }
    }
    int del_min(){
        int return_num = heap[1];
        heap[1] = heap[size];
        size--;
        heap.pop_back();
        perc_down(1);
        return return_num;
    }
    void perc_down(int idx){
        while(idx * 2 <= size){
            int min_child_idx = find_min_child_idx(idx);
            if(heap[idx] > heap[min_child_idx])
                swap(heap[idx], heap[min_child_idx]);
            idx = min_child_idx;
        }
    }
    int find_min_child_idx(int idx){
        // If no right child, return left child index
        int return_idx;
        if(idx * 2 + 1 > size)
            return_idx = idx * 2;
        else{
            if(heap[idx * 2] < heap[idx * 2 + 1])
                return_idx = idx * 2;
            else
                return_idx = idx * 2 + 1;
        }
        return return_idx;
    }
    void build_heap(vector <int> arr){
        size = arr.size();
        for(int i = 0; i < size; i++)
            heap.push_back(arr[i]);
        int idx = size / 2;
        while(idx > 0)
            perc_down(idx--);
    }
};


int main(void){
    srand(time(NULL));
    int size = 10;
    vector <int> arr;
    BinaryHeap bh;

    // If doing multiple insertion (O (n log n)), use below for loop.
    // for(int i = 0; i < size; i++){
    //     int rand_num = rand() % 100;
    //     arr.push_back(rand_num);
    //     bh.insert(rand_num);
    // }

    for(int i = 0; i < size; i++)
        arr.push_back(rand() % 100);

    bh.build_heap(arr);

    sort(arr.begin(), arr.end());
    for(int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;

    for(int i = 0; i < size; i++)
        cout << bh.del_min() << " ";
    cout << endl;
}
