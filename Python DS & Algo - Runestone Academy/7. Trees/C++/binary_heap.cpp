#include <iostream>
#include <vector>
using namespace std;

class BinaryHeap{
private:
    vector <int> heap;
    int size = 0;
public:
    BinaryHeap(){
        heap.push_back(0);
    }
    bool is_empty(){
        return (size == 0)? true : false;
    }
    void insert(int value){
        heap.push_back(value);
        int idx = ++size;
        while(heap[idx] < heap[idx/2] && idx > 0){
            swap(heap[idx], heap[idx/2]);
            idx /= 2;
        }
    }
    int get_size(){
        return size;
    }
    int find_min(){
        return heap[1];
    }
    int del_min(){
        int l_idx, r_idx, idx = 1, min_child_idx, return_val;
        return_val = heap[1];
        heap[1] = heap[size--];
        heap.pop_back();
        while(idx * 2 <= size){
            // finding smaller child
            l_idx = idx * 2;
            r_idx = idx * 2 + 1;
            if(r_idx > size)
                min_child_idx = idx*2;
            else
                (heap[l_idx] < heap[r_idx]) ? min_child_idx = l_idx : min_child_idx = r_idx;
            // If parent is bigger, swap with smaller child of the two childs
            if(heap[idx] > heap[min_child_idx]){
                swap(heap[idx], heap[min_child_idx]);
                idx = min_child_idx;
            }
            else break;
        }
        return return_val;
    }
    void build_heap(int * arr, int size){
        for(int i=0; i<size; i++)
            insert(arr[i]);
    }
};

int main(void){
    BinaryHeap bh;
}
