// Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

// Input:  Tact Coa
// Output: True (permutations: "taco cat", "atco cta". etc.)

// Page 60

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

// Solution 1
// Using a counter array.
// Assuming that character set only contains lowercase alphabets.
// Palindromes always have either one set of odd numbered paired letters and even numbered pairs of letters or all even numbered pairs of letters. We can use this to check whether there is more than one odd pair, in which case it is not a palindrome. This solution ignores spaces.
// Time Complexity: O(n), Space Complexity: O(1)
bool is_palindrome_permutation_1(string str){
    int counter[26] = {0}, index;
    for(auto ch : str){
        if(ch != ' '){
            index = ch - 'a';
            if(!counter[index]) counter[index]++;
            else counter[index]--;
        }
    }
    bool seen_one = false;
    for(auto ch : str){
        if(ch != ' '){
            index = ch - 'a';
            if(counter[index] && !seen_one) seen_one = true;
            else if(counter[index] && seen_one) return false;
        }
    }
    return true;
}

// Solution 2
// Using a hashmap
// If the number of odd pairs are more than 1, return false
// Time Complexity: O(n), Space Complexity: O(m) where m is the number of unique characters in the string.
bool is_palindrome_permutation_2(string str){
    unordered_map <char, int> hashmap;
    for(auto ch : str){
        if(ch != ' '){
            if(hashmap.find(ch) != hashmap.end()) hashmap[ch]++;
            else hashmap[ch] = 1;
        }
    }
    int odd_count = 0;
    for(auto ch : str){
        if(ch != ' '){
            if(hashmap[ch] % 2 != 0) odd_count++;
            if(odd_count > 1) return false;
        }
    }
    return odd_count <= 1;
}

// Solution 3
// Using a bit vector
// Time Complexity: O(n), Space Complexity: O(1)
bool is_palindrome_permutation_3(string str){
    int char_value, bit_vector = 0;
    for(auto ch : str){
        if(ch != ' '){
            char_value = ch - 'a';
            if((bit_vector & (1 << char_value)) == 0) bit_vector |= (1 << char_value); //  Only evaluates to zero if bit was not set
            else bit_vector &= ~(1 << char_value);  // Toggles bit which is at char_value's place
        }
    }
    // If a bit vector has only one 1, ANDing it with (itself - 1) will give 0. If there is more than one 1, it won't give a 0.
    return (bit_vector == 0 || (bit_vector & (bit_vector - 1)) == 0);
}

int main(void){
}
