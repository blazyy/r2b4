// Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

// Page 60

// What makes this problem not so easy is that you don't want to count the zeroes that came as a result of another 0.

#include <iostream>
#include <set>
using namespace std;
const int n = 4;

void print_matrix(int matrix[][n]){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << matrix[i][j] <<  ' ';
        }
        cout << endl;
    }
}

// Solution 1
// Keeping track of rows and cols that have 0 by traversing through the matrix and setting them later
// Time Complexity: O(n^2), Space Complexity: O(n)
void zero_matrix_1(int matrix[][n]){
    set <int> rows;
    set <int> cols;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(matrix[i][j] == 0){
                rows.insert(i);
                cols.insert(j);
            }
        }
    }
    for(auto row : rows)
        for(int col = 0; col < n; col++)
            matrix[row][col] = 0;
    for(auto col : cols)
        for(int row = 0; row < n; row++)
            matrix[row][col] = 0;
    print_matrix(matrix);
}

// Solution 2
// Use first column to store columns with zeroes and first row to store rows with zeroes. Preemptively scan first row and column to check if they have zeroes before replacing them.
// Time Complexity: O(n^2), Space Complexity: O(1)
void zero_matrix_2(int matrix[][n]){
    bool first_row_has_zero = false;
    bool first_col_has_zero = false;
    // Checking if first row has any zeros
    for(int col = 0; col < n; col++){
        if(matrix[0][col] == 0){
            first_row_has_zero = true;
            break;
        }
    }
    // Checking if first column has any zeros
    for(int row = 0; row < n; row++){
        if(matrix[row][0] == 0){
            first_col_has_zero = true;
            break;
        }
    }
    // Check if rest of the array has zeros. We can't start setting zeroes here since new zeroes will be counted as zeroes that already existed
    for(int row = 1; row < n; row++){
        for(int col = 1; col < n; col++){
            if(matrix[row][col] == 0){
                matrix[row][0] = 0;
                matrix[0][col] = 0;
            }
        }
    }
    // Setting rows to zero
    for(int row = 1; row < n; row++){
        if(matrix[row][0] == 0){
            for(int col = 1; col < n; col++){
                matrix[row][col] = 0;
            }
        }
    }
    // Setting columns to zero
    for(int col = 1; col < n; col++){
        if(matrix[0][col] == 0){
            for(int row = 1; row < n; row++){
                matrix[row][col] = 0;
            }
        }
    }
    // Setting first row to zeros if it initially had zeros
    if(first_row_has_zero)
        for(int col = 0; col < n; col++)
            matrix[0][col] = 0;

    // Setting first column to zeros if it initially had zeros
    if(first_col_has_zero)
        for(int row = 0; row < n; row++)
            matrix[row][0] = 0;
    print_matrix(matrix);
}

int main(void){
    int matrix[n][n] = {{1, 2, 3, 4},
                        {5, 6, 7, 8},
                        {9, 0, 11, 12},
                        {13, 14, 15, 16}};

    // zero_matrix_1(matrix);
    zero_matrix_2(matrix);
}
