"""
By: Nicolas Andrés Bolaños Fernandez / sep-2025
This algorithm determines the minimum n_0 for which P(x) >= 0  for all x >= n_0 
"""
T = int(input())

for _ in range(T):
    A = [int(x) for x in input().split(" ")]
    A.reverse()
    c = 0

    while True:
        c = c+1
        Q = A[0]
        seguir = True
        
        for i in range(len(A)-1):
            Q = Q*c + A[i+1]
            if Q < 0:
                seguir = False
                break
        
        if not seguir:
            continue
        else:
            print(c)
            break