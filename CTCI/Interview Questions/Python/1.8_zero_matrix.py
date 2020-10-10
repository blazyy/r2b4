# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# Page 60

# What makes this problem not so easy is that you don't want to count the zeroes that came as a result of another 0.

def print_matrix(mat):
    for row in range(len(mat)):
        print(mat[row])

# Solution 1
# Keeping track of rows and cols that have 0 by traversing through the matrix and setting them later
# Time Complexity: O(n^2), Space Complexity: O(n)
def zero_matrix_1(mat):
    n = len(mat)
    zero_rows = set()
    zero_cols = set()
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for row in zero_rows:
        for col in range(n):
            mat[row][col] = 0
    for col in zero_cols:
        for row in range(n):
            mat[row][col] = 0
    return mat

# Solution 2
# Use first column to store columns with zeroes and first row to store rows with zeroes. Preemptively scan first row and column to check if they have zeroes before replacing them.
# Time Complexity: O(n^2), Space Complexity: O(1)
def zero_matrix_2(mat):

    def set_row_to_zero(mat, row_idx, starting_col_idx):
        n = len(mat)
        for col in range(starting_col_idx, n):
            mat[row_idx][col] = 0

    def set_col_to_zero(mat, starting_row_idx, col_idx):
        n = len(mat)
        for row in range(starting_row_idx, n):
            mat[row][col_idx] = 0

    n = len(mat)
    first_row_has_zero = False
    first_col_has_zero = False
    # Checking if first row has any zeros
    for col in range(n):
        if mat[0][col] == 0:
            first_row_has_zero = True
            break
    # Checking if first column has any zeros
    for row in range(n):
        if mat[row][0] == 0:
            first_col_has_zero = True
            break

    # Check if rest of the array has zeros. We can't start setting zeroes here since new zeroes will be counted as zeroes that already existed
    for row in range(1, n):
        for col in range(1, n):
            if mat[row][col] == 0:
                mat[row][0] = 0
                mat[0][col] = 0

    # Setting rows to zero
    for row in range(1, n):
        if mat[row][0] == 0:
            set_row_to_zero(mat, row, 1)

    # Setting cols to zero
    for col in range(1, n):
        if mat[0][col] == 0:
            set_col_to_zero(mat, 1, col)

    # Setting first row to zeros if it initially had zeros
    if first_row_has_zero:
        set_row_to_zero(mat, 0, 0)

    # Setting first col to zeros if it initially had zeros
    if first_col_has_zero:
        set_col_to_zero(mat, 0, 0)

    return mat

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 16]]
print_matrix(zero_matrix_2(mat))
