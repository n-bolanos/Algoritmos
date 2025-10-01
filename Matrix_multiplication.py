"""
By: Nicolas Andrés Bolaños Fernandez / sep-2025
This code is the implementation of a recursive in-place algorithm to
solve matrix multiplications (Cormen, 4th edition)

Input: Matrices A and B, and an initialized matrix of zeros to return the answer -C-, 
as well as the size of the matrixes.
Output: None (The result is now in C)
"""
def matrix_multiply_recursive(A, B, C, n):
    if n == 1: #Base case
        C[0][0] = C[0][0] + A[0][0] * B[0][0]
        return

    #Divide
    mid = n//2

    A11 = A[:mid]
    for  i in range(mid):
        A11[i] = A11[i][:mid]

    A12 = A[:mid]
    for  i in range(mid):
        A12[i] = A12[i][mid:]

    A21 = A[mid:]
    for  i in range(mid):
        A21[i] = A21[i][:mid]

    A22 = A[mid:]
    for  i in range(mid):
        A22[i] = A22[i][mid:]

    B11 = B[:mid]
    for  i in range(mid):
        B11[i] = B11[i][:mid]

    B12 = B[:mid]
    for  i in range(mid):
        B12[i] = B12[i][mid:]

    B21 = B[mid:]
    for  i in range(mid):
        B21[i] = B21[i][:mid]

    B22 = B[mid:]
    for  i in range(mid):
        B22[i] = B22[i][mid:]

    C11 = C[:mid]
    for  i in range(mid):
        C11[i] = C11[i][:mid]

    C12 = C[:mid]
    for  i in range(mid):
        C12[i] = C12[i][mid:]

    C21 = C[mid:]
    for  i in range(mid):
        C21[i] = C21[i][:mid]

    C22 = C[mid:]
    for  i in range(mid):
        C22[i] = C22[i][mid:]

    matrix_multiply_recursive(A11, B11, C11, mid)
    matrix_multiply_recursive(A11, B12, C12, mid)
    matrix_multiply_recursive(A21, B11, C21, mid)
    matrix_multiply_recursive(A21, B12, C22, mid)
    matrix_multiply_recursive(A12, B21, C11, mid)
    matrix_multiply_recursive(A12, B22, C12, mid)
    matrix_multiply_recursive(A22, B21, C21, mid)
    matrix_multiply_recursive(A22, B22, C22, mid)

    for i in range(mid):
        C[i][:mid] = C11[i]
        C[i][mid:] = C12[i]
    for i in range(mid):
        C[i+mid][:mid] = C21[i]
        C[i+mid][mid:] = C22[i]
    return


A = [[1, 5, 1, 5], [2, 6, 2, 6], [3, 7,3,7], [4, 8, 4, 8]]
B = [[1,2, 3,4 ], [5, 6,7, 8], [1,2, 3,4 ], [5, 6,7, 8]]
C = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

matrix_multiply_recursive(A, B, C, 4)
print(C)
