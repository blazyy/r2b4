// Assume you have a mthod isSubstring which cheks if one word is a substring of another. Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

// Example: "waterbottle" is a rotation of "erbottlewat"

// Page 61

#include <iostream>
using namespace std;

// Page 61

// Solution
// Double s1 and check if s2 in s1 using isSubstring
// waterbottle -> waterbottlewaterbottle. 'erbottlewa' exists in doubled s1.
// Time Complexity: O(n), Space Complexity: O(n)
bool is_string_rotation(string s1, string s2){
    s1 += s1;
    return s1.find(s2) != string::npos;
}

int main(void){
    cout << is_string_rotation("waterbottle", "erbottlewa") << endl;
    cout << is_string_rotation("waterbottle", "erbttlwea") << endl;
}
