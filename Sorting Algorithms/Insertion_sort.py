"""
By: Nicolas Andrés Bolaños Fernandez / sep-2025
This code is the implementation of the well-known algorithm Insertion Sort (Cormen, 4th edition)

Input: An array of unordered numbers separated by spaces
Output: The same array but ordered in ascending order
"""
A = [int(x) for x in input().split(" ")]
n = len(A)

for i in range(1, n):
    key = A[i]
    j = i -1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = key

print(A)
