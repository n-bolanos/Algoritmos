"""
By: Nicolas Andrés Bolaños Fernandez / sep-2025
This code is the implementation of a recursive in-place algorithm to
solve matrix multiplications (Cormen, 4th edition)

Input: Matrices A and B, and an initialized matrix of zeros to return the answer -C-, 
as well as the size of the matrixes.
Output: None (The result is now in C)
"""
def matrix_multiply_recursive(A, row_a, col_a, B, row_b, col_b, C, row_c, col_c, n):
    if n == 1: #Base case
        C[row_c-1][col_c-1] += A[row_a-1][col_a-1] * B[row_b-1][col_b-1]
        return

    #Divide
    mid = n//2

    row_a11, col_a11 = row_a, col_a
    row_a12, col_a12 = row_a, col_a + mid
    row_a21, col_a21 = row_a+mid, col_a
    row_a22, col_a22 = row_a+mid, col_a + mid

    row_b11, col_b11 = row_b, col_b
    row_b12, col_b12 = row_b, col_b + mid
    row_b21, col_b21 = row_b+mid, col_b
    row_b22, col_b22 = row_b+mid, col_b + mid

    row_c11, col_c11 = row_c, col_c
    row_c12, col_c12 = row_c, col_c + mid
    row_c21, col_c21 = row_c+mid, col_c
    row_c22, col_c22 = row_c+mid, col_c + mid


    matrix_multiply_recursive(A, row_a11, col_a11, B, row_b11, col_b11, C, row_c11, col_c11, mid)
    matrix_multiply_recursive(A, row_a11, col_a11, B, row_b12, col_b12, C, row_c12, col_c12, mid)
    matrix_multiply_recursive(A,row_a21, col_a21, B, row_b11, col_b11, C, row_c21, col_c21, mid)
    matrix_multiply_recursive(A, row_a21, col_a21, B, row_b12, col_b12, C, row_c22, col_c22, mid)
    matrix_multiply_recursive(A, row_a12, col_a12, B, row_b21, col_b21, C, row_c11, col_c11, mid)
    matrix_multiply_recursive(A, row_a12, col_a12, B, row_b22, col_b22, C, row_c12, col_c12, mid)
    matrix_multiply_recursive(A, row_a22, col_a22, B, row_b21, col_b21, C, row_c21, col_c21, mid)
    matrix_multiply_recursive(A, row_a22, col_a22, B, row_b22, col_b22, C, row_c22, col_c22, mid)


A = [[1, 5, 1, 5], [2, 6, 2, 6], [3, 7,3,7], [4, 8, 4, 8]]
B = [[1,2, 3,4 ], [5, 6,7, 8], [1,2, 3,4 ], [5, 6,7, 8]]
C = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

matrix_multiply_recursive(A, 1, 1, B, 1, 1, C, 1, 1, 4)
print(C)
