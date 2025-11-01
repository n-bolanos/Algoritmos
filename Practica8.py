def partition(A, p, r):
    x = A[r]
    i = p-1

    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1

def selection_sort(A, p, r):
    #Encontrar el máximo
    max = p
    for i in range(p+1, r+1):
        if A[i]>A[max]:
            max = i
    
    A[r], A[max] = A[max], A[r] #Intercambiar le máximo con el último
    quicksort_modified(A, p, r-1)

def quicksort_modified(A, p, r):
    if r-p < 1:
        return None
    elif r-p < 7:
        print(*A[p:r+1])
        selection_sort(A, p, r)
    else:
        q = partition(A, p, r)
        print(A[q])
        quicksort_modified(A, p, q-1)
        quicksort_modified(A, q+1,r)
    



A = [int(x) for x in input().split()]
quicksort_modified(A, 0, len(A)-1)

print(*A)