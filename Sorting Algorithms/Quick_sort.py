"""
By: Nicolas Andrés Bolaños Fernandez / nov-2025
This code is the implementation of the well-known recursive 
algorithm Quick Sort (Cormen, 4th edition)

Input: An array of unordered numbers separated by spaces
Output: The same array but ordered in ascending order
"""

from random import randint

def randomizedPartition(A, p, r):
    i = randint(p,r)
    A[r], A[i] =  A[r], A[i]
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r] # Calcular pivote
    i = p-1     # Mayor índice en el lado de números menores al pivote

    for j in range(p, r):
        if A[j] <= x:   # Es este elemento menor o igual al pivote?
            i = i+1
            A[i], A[j] = A[j], A[i] # Ponerlo al lado del arreglo que correcponde
    A[i+1], A[r] = A[r], A[i+1] # Se mueve el pivote desde el final del arreglo a su posición final

    return i+1  #Índice del pivote

def quicksort(A, p, r):
    if p < r:
        #Elegir el pivote y organizar los número respecto a este
        q = randomizedPartition(A, p, r)
        quicksort(A, p, q-1)    #Ordenar sub-arreglo izqueirdo
        quicksort(A, q+1,r) #Ordenar sub-arreglo derecho

A = [int(x) for x in input().split(" ")]
quicksort(A, 0, len(A)-1)

print(*A)