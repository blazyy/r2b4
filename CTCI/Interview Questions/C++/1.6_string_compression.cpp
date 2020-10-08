// Implement a method to perform basic string compression using the counts of repeated characters. For example, the string 'aabccccaaa' would become 'a2b1c4a3'. If the "compressed" string would not become smaller from the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters

// Page 60

#include <iostream>
using namespace std;

// Solution 1
// For loop
// One downside here is that we build the string without checking if compression will actually reduce the length of the string. If the string has many non repeating character sequences, we would've wasted space by building a string which we'd never use.
// Time Complexity: O(n) Space Complexity: I don't think it makes sense to mention this here.
string compress_string_1(string str){
    string comp_str = "";
    char current_char = str[0];
    comp_str += current_char;
    int count = 1;
    for(int i = 1; i < str.length(); i++){
        if(str[i] == current_char) count++;
        else{
            current_char = str[i];
            comp_str += to_string(count);
            comp_str += current_char;
            count = 1;
        }
    }
    comp_str += to_string(count);
    if(comp_str.length() > str.length()) return str;
    return comp_str;
}

int count_consecutives(string str){
    int consec_counts = 1;
    char current_char = str[0];
    for(int i = 1; i < str.length(); i++){
        if(str[i] != current_char){
            consec_counts++;
            current_char = str[i];
        }
    }
    return consec_counts;
}

// Solution 2
// Counting the size of the compressed string beforehand so that we don't unnecessarily start creating a new string. Downsize is that it needs to iterate through the string twice. Another advantage here is that we already know the final size of the string, so could be more efficient by allocating size for the to-be-compressed string.
// Time Complexity: O(n), Space Complexity: I don't think it makes sense to mention this here.
string compress_string_2(string str){
    if(count_consecutives(str) * 2 >= str.length()) return str;
    // Could allocate a string/character array of fixed size using the value returned from count_consecutives but I'm too lazy to implement that now. String insertions have O(1) amortized time, so while there will be difference it will be small.
    string comp_str = "";
    char current_char = str[0];
    comp_str += current_char;
    int count = 1;
    for(int i = 1; i < str.length(); i++){
        if(str[i] == current_char) count++;
        else{
            current_char = str[i];
            comp_str += to_string(count);
            comp_str += current_char;
            count = 1;
        }
    }
    comp_str += to_string(count);
    return comp_str;
}

int main(void){
    cout << compress_string_1("aabccccaaa") << endl;
    cout << compress_string_2("aabccccaaa") << endl;
    cout << compress_string_1("abcdefhigj") << endl;
    cout << compress_string_2("abcdefhigj") << endl;
}
