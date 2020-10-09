// Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

// Page 60

#include <iostream>
using namespace std;
const int n = 10;

void print_matrix(int matrix[][n]){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << matrix[i][j] <<  ' ';
        }
        cout << endl;
    }
}

//   Solution 1 (Bad)
//   Using an auxiliary array
//   Time Complexity: O(n^2), Space Complexity: O(n^2)
void rotate_matrix_1(int mat[][n]){
    // Not implementing a check to see if the matrix is square since I'm generating the matrix myself but just imagine that the condition exists here. Thx for imagining.
    int rmat[n][n];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            rmat[i][j] = mat[n-j-1][i];
    print_matrix(rmat);
}

// Solution 2
// Transpose matrix and rearrange columns inplace
// Time Complexity: O(n^2), Space Complexity: O(1)
void rotate_matrix_2(int mat[][n]){
    // Not implementing a check to see if the matrix is square since I'm generating the matrix myself but just imagine that the condition exists here. Thx for imagining.
    for(int i = 0; i < n; i++)
        for(int j = i; j < n; j++)
            if(i != j)
                swap(mat[i][j], mat[j][i]);
    int start = 0, end = n - 1;
    while(start < end){
        for(int i = 0; i < n; i++)
            swap(mat[i][start], mat[i][end]);
        start++;
        end--;
    }
    print_matrix(mat);
}

int main(void){
    int matrix[n][n];
    int count = 1;
    // Create an nxn matrix
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            matrix[i][j] = count++;

    rotate_matrix_1(matrix);
    cout << endl;
    rotate_matrix_2(matrix);
}
