"""
By: Nicolas Andrés Bolaños Fernandez / sep-2025
This code is the implementation of Strassen's recursive algorithm
to solve matrix multiplications (based on Cormen, 4th edition and Strassen 1969)

Input: Matrixes A and B (square, power of 2 dimension)
Output: New matrix C = A*B
"""

def add_matrix(X, Y):
    """Addition of two matrices."""
    n = len(X)
    Z = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = X[i][j] + Y[i][j]
    return Z

def sub_matrix(X, Y):
    """Subtraction of two matrices."""
    n = len(X)
    Z = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = X[i][j] - Y[i][j]
    return Z

def strassen(A, B):
    n = len(A)
    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide matrices into quadrants
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Compute S matrices
    S1  = sub_matrix(B12, B22)
    S2  = add_matrix(A11, A12)
    S3  = add_matrix(A21, A22)
    S4  = sub_matrix(B21, B11)
    S5  = add_matrix(A11, A22)
    S6  = add_matrix(B11, B22)
    S7  = sub_matrix(A12, A22)
    S8  = add_matrix(B21, B22)
    S9  = sub_matrix(A11, A21)
    S10 = add_matrix(B11, B12)

    # Compute P matrices recursively
    P1 = strassen(A11, S1)
    P2 = strassen(S2, B22)
    P3 = strassen(S3, B11)
    P4 = strassen(A22, S4)
    P5 = strassen(S5, S6)
    P6 = strassen(S7, S8)
    P7 = strassen(S9, S10)

    # Compute C quadrants
    C11 = add_matrix(sub_matrix(add_matrix(P5, P4), P2), P6)
    C12 = add_matrix(P1, P2)
    C21 = add_matrix(P3, P4)
    C22 = sub_matrix(sub_matrix(add_matrix(P5, P1), P3), P7)

    # Combine quadrants into result
    C = [[0]*n for _ in range(n)]
    for i in range(mid):
        C[i][:mid] = C11[i]
        C[i][mid:] = C12[i]
    for i in range(mid):
        C[i+mid][:mid] = C21[i]
        C[i+mid][mid:] = C22[i]

    return C



A = [[1, 5, 1, 5],
    [2, 6, 2, 6],
    [3, 7, 3, 7], 
    [4, 8, 4, 8]]
B = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8]]

C = strassen(A, B)
print(C)
