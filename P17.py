def floyd_w(W, O):
    n = len(W)
    D = [[[0 if i == j else float("inf") for i in range(n)] for j in range(n)] for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            D[0][i][j] = W[i][j]

    P = [[[None for i in range(n)] for j in range(n)] for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            P[0][i][j] = O[i][j]

    for k in range(1, n + 1):
        puente = k - 1
        for i in range(n):
            for j in range(n):
                nuevo_camino = D[k-1][i][puente] + D[k-1][puente][j]
                
                if nuevo_camino < D[k-1][i][j]:
                    D[k][i][j] = nuevo_camino
                    P[k][i][j] = P[k-1][puente][j]
                else:
                    D[k][i][j] = D[k-1][i][j]
                    P[k][i][j] = P[k-1][i][j]
    
    for i in range(n):
        for j in range(n):
            if i == j and D[-1][i][j] != 0:
                return "Negative cycle"
                    
    return D[-1], P[-1]

config = [int(i) for i in input().split()]
W = [[float("inf") for _ in range(config[0])] for _ in range(config[0])]
O = [[None for _ in range(config[0])] for _ in range(config[0])]

for i in range(config[0]):
    W[i][i] = 0
    O[i][i] = None

for _ in range(config[1]):
    u, v, w = [int(i) for i in input().split()]
    W[u][v] = w
    O[u][v] = u

respuesta = floyd_w(W, O)

if type(respuesta) is str:
    print(respuesta)
else:
    d, p = respuesta
    print('D')
    for i in d:
        print(*i)
    print('Pi')
    for i in p:
        print(*i)