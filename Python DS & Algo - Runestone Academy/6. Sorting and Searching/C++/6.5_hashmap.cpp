#include <iostream>
using namespace std;

class HashMap{
private:
    int size = 11;
    int * slots = new int[size];
    string * items = new string[size];
public:
    HashMap(){
        for(int i = 0; i < size; i++){
            slots[i] = INT_MIN;
            items[i] = "NULL";
        }
    }
    int hash(int key){
        if(key < 0)
            key = size + key;
        return key % size;
    }
    int rehash(int old_hash, int skip = 1){
        return (old_hash + skip) % size;
    }
    void put(int key, string value){
        int hash_value = hash(key);
        while(slots[hash_value] != INT_MIN && slots[hash_value] != key)
            hash_value = rehash(hash_value);
        if(slots[hash_value] == INT_MIN)
            slots[hash_value] = key;
        items[hash_value] = value;
    }
    string get(int key){
        int hash_value = hash(key);
        int first_hash = hash_value;
        while(slots[hash_value] != INT_MIN && slots[hash_value] != key){
            hash_value = rehash(hash_value);
            if(hash_value == first_hash)
                return "NULL";
        }
        return items[hash_value];
    }
    void print(){
        cout << '{';
        for(int i = 0; i < size; i++){
            if(slots[i] != INT_MIN){
                cout << slots[i] << ": '" << items[i] << "'";
                if(i != size - 1)
                    cout << ", ";
            }
        }
        cout << '}';
    }
};

int main(void){
    HashMap H;
    H.put(-1, "cattus maximus");
    H.put(26, "dog");
    H.put(93, "lion");
    H.put(17, "tiger");
    H.put(77, "bird");
    H.put(31, "cow");
    H.put(44, "goat");
    H.put(55, "pig");
    H.put(20, "chicken");
    H.put(20, "duck");
    H.print();
}
