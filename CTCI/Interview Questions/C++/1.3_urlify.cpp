// Write a method to replace all spaces in a string with '%20'. You may assume that the string
// has sufficient space at the end to hold the additional characters, and that you are given
//  the "true" length of the string. (Note: If implementing in Java, please use a character
// array so that you can perform this operation in place)

// Page 60

// Input:  "Mr John Smith     ", 13
// Output: "Mr%20John%20Smith"

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

// Working backwards from the end of string, since there's extra spaces and we don't have to worry about overrwriting any characters.
// First, calculate the index from where to start rewriting from by adding true length and 2 * original spaces in the 'true' string
// Starting from this index, if a space occurs, replace with '%20', else replace with character of index i where i starts from true length - 1and goes till 0
// Time Complexity: O(n), Space Complexity: O(1)
string urlify(string str, int true_length){
    int space_count = 0;
    for(int i = 0; i < true_length; i++)
        if(str[i] == ' ')
            space_count++;
    int index = true_length + space_count * 2;
        if(str[i] == ' '){
            str[index - 1] = '0';
            str[index - 2] = '2';
            str[index - 3] = '%';
            index -= 3;
        } else{
            str[index - 1] = str[i];
            index--;
        }
    }
    return str;
}

int main(void){
    cout << urlify("Mr John Smith     ", 13);
}
