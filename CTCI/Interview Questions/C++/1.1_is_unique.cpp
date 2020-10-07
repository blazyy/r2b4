//  Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
// Page 60

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

// Solution 1:
// Using a hashmap.
// Time complexity: O(n), Space Complexity: O(n)
bool is_unique_1(string str){
    if(str.length() > 128) return false;
    unordered_map <char, bool> map;
    for(auto ch : str){
        if(map.find(ch) != map.end())
            return false;
        map[ch] = true;
    }
    return true;
}

// Solution 2:
// Sorting the input string.
// Time Complexity: O(n log n), Space Complexity: O(1).
// Note: Modifies input string.
bool is_unique_2(string str){
    if(str.length() > 128) return false;
    sort(str.begin(), str.end());
    for(int i = 0; i < str.length() - 1; i++)
        if(str[i] == str[i + 1])
            return false;
    return true;
}

// Solution 3.
// Using a character set. Here, assuming string has only lowercase alphabets but this can be extended as needed.
// Time Complexity: O(n), Space Complexity: 0(1) if fixed character set, else O(c) or O(min(c, n)) where c is the size of character set.
bool is_unique_3(string str){
    if(str.length() > 128) return false;
    int num_chars = 26;
    bool char_set[num_chars];
    for(int i = 0; i < num_chars; i++)
        char_set[i] = false;
    for(auto ch : str){
        int index = ch - 'a';
        if(char_set[index])
            return false;
        char_set[index] = true;
    }
    return true;
}

// Solution 4:
// Using a bit vector (i.e. an int) and bit shifting.
// Time Complexity: O(n), Space Complexity: O(1).
// Only works for smallercase A-Z since integer can only hold 32 bits.
bool is_unique_4(string str){
    if(str.length() > 128) return false;
    int checker = 0;
    for(auto ch : str){
        int value = ch - 'a';
        if((checker & (1 << value)) > 0)
            return false;
        checker |= (1 << value);
    }
    return true;
}

int main(void){
}
