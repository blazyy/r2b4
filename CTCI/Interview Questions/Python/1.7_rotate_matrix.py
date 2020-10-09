# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# Page 60

# Solution 1 (Bad)
# Using an auxiliary array
# Time Complexity: O(n^2), Space Complexity: O(n^2)
def rotate_matrix_1(mat):
    if len(mat) != len(mat[0]):
        return mat
    n = len(mat)
    rmat = [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(n):
        for j in range(n):
            rmat[i][j] = mat[n-j-1][i]
    return rmat

# Solution 2
# Transpose matrix and rearrange columns inplace
# Time Complexity: O(n^2), Space Complexity: O(1)
def rotate_matrix_2(mat):
    if len(mat) != len(mat[0]):
        return mat
    n = len(mat)
    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            if i != j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Rearrange columns
    start = 0
    end = n - 1
    while start < end:
        for i in range(n):
            mat[i][start], mat[i][end] = mat[i][end], mat[i][start]
        start += 1
        end -= 1
    return mat

print(rotate_matrix_1([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate_matrix_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
