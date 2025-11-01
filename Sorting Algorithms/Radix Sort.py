
# def porcionar_numero(num, d, r):
#     """Función encargada de determinar la partición de un número.
#     Implementación inefciente, pero mía"""
#     try:
#         if d == 0:
#             if r <= len(bin(num))-2:
#                 return int(bin(num)[-r:], 2)
#             else:
#                 print(num)
#                 return num
        
#         binario = bin(num)[2:]
#         return int(binario[-(d+1)*r:-(d)*r], 2)
#     except:
#         return 0
    
def porcionar_numero(num, d, r):
    """ Esta función se encarga de determinar la partición en bits de un número.
    Implementación más eficiente (dada por ChatGPT)
    """
    mask = (1 << r) - 1
    return (num >> (d * r)) & mask
        
def modified_counting_sort(A, k, d, r):
    """
    Implementación de un algoritmo estable lineal (Counting Sort)
    modificado para revisar por particiones de los números.
    A -> lista con los números originales
    k -> Máxima paritición
    d -> Se organizará por la d-ésima partición de los números
    r -> tamaño de la partición
    """
    B = [0 for _ in range(len(A))]
    C = [0 for _ in range(k+1)]

    for j in range(len(A)):
        number = porcionar_numero(A[j], d, r)
        C[number] += 1
    # At this point, C[i] contains the number of elements equal to i

    for i in range(1, k+1):
        C[i] += C[i-1]
    # Now C[i] contains the number of elements less than or equal to i

    for j in range(len(A)-1, -1, -1):
        number = porcionar_numero(A[j], d, r)
        B[C[number]-1] = A[j]
        C[number] -= 1
    
    return B

def radix_sort(A, r=1):
    """
    Implementación de RadixSort
    A -> Arreglo a ordenar
    r -> tamaño de las particiones para ordenar los números en bits"""
    d = max([len(bin(n))-2 for n in A])

    for i in range(0, (d//r + 1), 1):
        tmp = []
        for elemento in A:
            tmp.append(porcionar_numero(elemento, i, r))
        
        k = max(tmp)
        A = modified_counting_sort(A, k, i, r)

    return A

#A = [20, 31, 16, 41, 5, 20, 4, 1, 0]
#A = [9,8,7,6,5,4,3,2,1]
#A=[3, 1, 2]
#A = [1201, 810, 809,] #Representa fechas, y usa un r=16
r = int(input("Tamaño de las particiones en bits: "))
A = [int(x) for x in input().split()]
A = radix_sort(A, r)
print(*A)