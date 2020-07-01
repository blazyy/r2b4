#include<iostream>
using namespace std;

int recursive_factorial(int num){
    if(num <= 1)
        return 1;
    return num * recursive_factorial(num - 1);
}

int main(void){
    cout << recursive_factorial(0) << endl;
}
