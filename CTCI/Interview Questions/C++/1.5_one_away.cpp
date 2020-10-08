// There are three types of edits that can be performed on strings: insert a character, remove a character, or
// replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away

// pale,  ple  -> true
// pales, pale -> true
// pale,  bale -> true
// pale,  nake -> false

// Page 60

#include <iostream>
#include <unordered_map>
#include <cstdlib> // contains llabs() functions
using namespace std;

// Solution 1
// Double for loop. Check if atleast n-1 characters from one string exists in the other
// Time Complexity: O(n^2), Space Complexity: O(1)
bool one_away_1(string str1, string str2){
    if(llabs(str1.length() - str2.length()) > 1) return false; // llabs is long long abs. Needed since length() returns a long long int.
    int count = 0;
    for(auto ch1 : str1)
        for(auto ch2 : str2)
            if(ch1 == ch2) count++;
    int higher_len = max(str1.length(), str2.length());
    return count >= higher_len - 1;
}

// Solution 2
// Hashmap. Check if atleast n-1 characters of bigger string are there in smaller string. If equal, check if more than one character difference.
// Time Complexity: O(n), Space Complexity: O(n)
bool one_away_2(string str1, string str2){
    if(llabs(str1.length() - str2.length()) > 1) return false;
    unordered_map <char, char> hashmap;
    for(auto ch : str1)
        if(hashmap.find(ch) == hashmap.end())
            hashmap[ch] = ' ';
    int count = 0;
    for(auto ch : str2)
        if(hashmap.find(ch) != hashmap.end())
            count++;
    return max(str1.length(), str2.length()) - count <= 1;
}

// Solution 3
// Single for loop
// If more than one difference found, return false
// Time Complexity: O(n), Space Complexity: O(1)
bool one_away_3(string str1, string str2){
    if(llabs(str1.length() - str2.length()) > 1) return false;
    if(str2.length() < str1.length()) swap(str1, str2);
    int index1 = 0, index2 = 0;
    bool found_diff = false;
    while(index1 < str1.length() && index2 < str2.length()){
        if(str1[index1] == str2[index2]) index1++;
        else{
            if(found_diff) return false;
            found_diff = true;
            if(str1.length() == str2.length()) index1++;
        }
        index2++;
    }
    return true;
}

int main(void){
    cout << one_away_1("pale", "ple");
    cout << one_away_1("pales", "pale");
    cout << one_away_1("pale", "bale");
    cout << one_away_1("pale", "bake") << endl;
    cout << one_away_2("pale", "ple");
    cout << one_away_2("pales", "pale");
    cout << one_away_2("pale", "bale");
    cout << one_away_2("pale", "bake") << endl;
    cout << one_away_3("pale", "ple");
    cout << one_away_3("pales", "pale");
    cout << one_away_3("pale", "bale");
    cout << one_away_3("pale", "bake") << endl;
}
