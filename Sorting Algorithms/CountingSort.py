"""
By: Nicolas Andrés Bolaños Fernandez / oct-2025
This code is the implementation of the linear sorting algorithm 
Counting Sort according to Cormen's pseudocode (Cormen, 4th edition)

Input: An array of unordered numbers separated by spaces
Output: The same array but ordered in ascending order
"""
def counting_sort(A, B, k):
    C = [0 for _ in range(k+1)]

    for j in range(len(A)):
        C[A[j]] += 1
    # At this point, C[i] contains the number of elements equal to i

    for i in range(1, k+1):
        C[i] += C[i-1]
    # Now C[i] contains the number of elements less than or equal to i

    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

A = [int(x) for x in input().split()]
B = [0 for _ in range(len(A))]

counting_sort(A, B, max(A))

print(*B)
    
    