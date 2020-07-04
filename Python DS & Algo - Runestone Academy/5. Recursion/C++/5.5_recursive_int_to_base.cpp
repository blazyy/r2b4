#include <iostream>
#include <cstring>
using namespace std;

int size = 10, idx = size - 1;
char * base_number = new char[size];
char digits[] = "0123456789ABCDEF";

// My implementation is probably way too complicated. Well. I don't care.
// My current C++ knowledge isn't enough to attempt this properly.

char int_to_base(int num, int base){
    if(num < base) base_number[idx--] = digits[num];
    else{
        base_number[idx--] = digits[num % base];
        return int_to_base(num/base, base);
    }
    return 'x'; // To stop warnings. Functions won't reach here.
}

int main(void){
    int_to_base(98033, 16); //3D4
    for(int i = idx+1; i != size; i++) cout << base_number[i];
}
