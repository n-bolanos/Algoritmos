"""
By: Nicolas Andrés Bolaños Fernandez / sep-2025
This code is the implementation of the well-known recursive 
algorithm Merge Sort (Cormen, 4th edition)

Input: An array of unordered numbers separated by spaces
Output: The same array but ordered in ascending order
"""
import math

def merge(A, p, q, r):
    '''
    Input: 
        A -> Original array of unordered numbers
        p -> Initial position of the left subarray
        q -> Final position of the left subarray
        r -> Final position of the right subarray
    Output: Ordered array A
    '''
    n_L = q-p+1 # length of A[p : q]
    n_R = r-q   # length of A[q + 1 : r]
    left = []
    right = []

    for i in range(n_L):
        left.append(A[p+i])   # copy A[p : q] into L[0 : nL – 1]
    for j in range(n_R):
        right.append(A[q + j +1])  # copy A[q + 1 : r] into R[0 : nR – 1]

    i=0 # i indexes the smallest remaining element in L
    j=0 # j indexes the smallest remaining element in R
    k=p # k indexes the location in A to fill

    # As long as each of the arrays L and R contains an unmerged element,
    # copy the smallest unmerged element back into A[p : r].

    while i < n_L and j < n_R:
        if left[i] < right[j]:
            A[k] = left[i]
            i = i+1
        else:
            A[k] = right[j]
            j = j+1
        k = k+1
    
    # Having gone through one of L and R entirely, copy the
    # remainder of the other to the end of A[p : r].
    while i < n_L:
        A[k] = left[i]
        i = i+1
        k = k+1
    while j < n_R:
        A[k] = right[j]
        j = j+1
        k = k+1

def merge_sort(A, p, r):
    '''
    Input:
        A -> Array of unordered numbers
        p -> initial position to start ordering
        r -> final position to order
    '''
    if p >= r:              # zero or one element?
        return
    q = math.floor((p+r)/2)      # midpoint of A[p : r]
    merge_sort(A, p, q)     # recursively sort A[p : q]
    merge_sort(A, q+1, r)   # recursively sort A[q + 1 : r]
    # Merge A[p : q] and A[q + 1 : r] into A[p : r].
    merge(A, p, q, r)

A = [int(x) for x in input().split(" ")]
merge_sort(A, 0, len(A)-1)

print(A)
