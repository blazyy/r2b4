// Check permutation: Given two strings, write a method to decided if one is a permutation of the other.
// Page 60

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

// Solution 1:
// Sorting both strings and checking if they are equal.
// Time complexity: O(n log n), Space Complexity: O(1)
bool check_permutation_1(string str1, string str2){
    if(str1.length() != str2.length()) return false;
    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());
    if(str1.compare(str2) == 0) return true;
    return false;
}

// Solution 2:
// Having a counter array for each string, and comparing all values in these counter arrays.
// Assuming characters are ASCII, so character set is 128 long.
// Time Complexity: O(n), Space Complexity: O(1) sinced charset is always of fixed length.
bool check_permutation_2(string str1, string str2){
    if(str1.length() != str2.length()) return false;
    int charset_length = 128;
    int counter[charset_length] = {0};
    for(int i = 0; i < str1.length(); i++)
        counter[str1[i] - 'a']++;
    for(int i = 0; i < str1.length(); i++){
        counter[str2[i] - 'a']--;
        if(counter[str2[i] - 'a'] < 0) return false;
    }
    return true;
}

// Solution 3
// Using a hashmap to store character counts. Using a hashmap here seems unnecessary but why the heck not?
// Time Complexity: O(n), Space Complexity: O(n)
bool check_permutation_3(string str1, string str2){
    if(str1.length() != str2.length()) return false;
    unordered_map <char, int> char_counts;
    for(auto ch : str1)
        if(char_counts.find(ch) != char_counts.end())
            char_counts[ch]++;
        else char_counts[ch] = 1;
    for(auto ch : str2){
        if(char_counts.find(ch) == char_counts.end()) return false;
        else{
            char_counts[ch]--;
            if(char_counts[ch] < 0) return false;
        }
    }
    return true;
}

int main(void){
}
