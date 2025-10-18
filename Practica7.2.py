"""
By: Nicolas Andrés Bolaños Fernandez / oct-2025
This algorithm simulates a minimum heap through 3 basic instructions:
- insertar x: inserts the number x in the heap
- extraer: extracts the head of the heap
- fin: ends the simulation

As input, it receives a set of instructions (until instruction "fin" is typed in)
It show the heap as it process the instruction, so the output look like this:
    instruction 1
    heap
    instruction 2
    heap
    instruction 3
    heap
    ...
    fin
"""
from math import floor
heap_size = 0

def parent(i):
    # Definición incorrecta, la correcta sería floor((i+1)/2) - 1 if i != 0 else 0
    return i//2

def left(i):
    return 2*(i+1) - 1

def right(i):
    return 2*(i+1)

def min_heapify(A, i):
    l = left(i)
    r = right(i)

    if l < heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    
    if r < heap_size and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def extract_min_heap(A: list):
    global heap_size

    if heap_size < 1:
        return None
    
    minimo = A[0]
    A[0] = A[heap_size -1]
    A.pop()
    heap_size -= 1
    min_heapify(A, 0)

    return minimo

def insert_min_heap(A: list, x):
    global heap_size

    if heap_size < 1:
        A.append(x)
        heap_size += 1
        return
    
    A.insert(heap_size, x)
    indice = heap_size
    heap_size += 1

    while A[parent(indice)] > x:
        A[indice], A[parent(indice)] = A[parent(indice)], A[indice]
        indice = parent(indice)
        if indice == 0:
            break

A = []
while True:
    try:
        entrada = input()
    except EOFError:
        break
    else: 
        inst = [i for i in entrada.split()]
        accion = inst[0]
    
        if accion == "insertar":
            elemento = int(inst[1])
            insert_min_heap(A, elemento)
            print(*A)

        elif accion == "extraer":
            head = extract_min_heap(A)
            if head is None:
                print("Empty")
            elif heap_size == 0:
                print("Empty")
            else:
                print(*A)

        elif accion == "fin":
            break
    

