
def porcionar_numero(num, d, r):
    """Función encargada de determinar la partición de un número.
    Implementación inefciente, pero mía"""
    try:
        if d == 0:
            if r <= len(bin(num))-2:
                return int(bin(num)[-r:], 2)
            else:
                return num

        binario = bin(num)[2:]
        return int(binario[-(d+1)*r:-(d)*r], 2)
    except:
        return 0


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


def radix_sort(A, b=None, r=1):
    """
    Implementación de RadixSort
    A -> Arreglo a ordenar
    r -> tamaño de las particiones para ordenar los números en bits"""
    if b is None:
        d = max([len(bin(n))-2 for n in A])
    else:
        d = b

    if d % r == 0:
        n = d//r
    else:
        n = d//r + 1

    for i in range(0, n):
        tmp = []
        for elemento in A:
            tmp.append(porcionar_numero(elemento, i, r))

        k = max(tmp)
        A = modified_counting_sort(A, k, i, r)
        print(*A)

    return A


datos = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A = radix_sort(A, datos[0], datos[1])
