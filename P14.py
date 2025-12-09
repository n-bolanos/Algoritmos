def bfs(G, s):
    C = []
    d = []
    p = []
    for vertice in range(len(G)):
        C.append("white")
        d.append(float("inf"))
        p.append(None)

    C[s] = "gray"
    d[s] = 0
    Q = [s]
    while len(Q) != 0:
        u = Q[0]
        for vertex in G[u]:
            if C[vertex] == "white":
                C[vertex] = "gray"
                d[vertex] = d[u] + 1
                p[vertex] = u
                Q.append(vertex)
        Q.pop(0)
        C[u] = "black"
    
    return p

def construir_camino(p, f, s):
    camino = "-> "+str(f)
    actual = f
    while p[actual] != None:
        padre = p[actual]
        camino = "-> " + str(padre) + camino
        actual = padre
    return camino[3:]



config = [int(i) for i in input().split()]
G = [[] for _ in range(config[0])]

for _ in range(config[1]):
    edge = [int(i) for i in input().split()]
    G[edge[0]].append(edge[1])

p = bfs(G, 0)

for i in range(0, len(p)):
    if p[i] is not None or i == 0:
        print(str(i)+"|"+construir_camino(p, i, 0))