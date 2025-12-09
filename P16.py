import heapq

def djkistra(G, r):
    key = {u: float('inf') for u in range(len(G))}
    p = {u: None for u in range(len(G))}
    encontrado = {u: False for u in range(len(G))}

    key[r] = 0
    Q = [(0, r)]

    while len(Q) != 0:
        peso, u = heapq.heappop(Q)

        if encontrado[u]:
            continue
        encontrado[u] = True

        for v, weight in G[u]:
            if not encontrado[v] and (weight+key[u]) < key[v]:
                p[v] = u
                key[v] = weight + key[u]
                heapq.heappush(Q, (key[v], v))
                
    
    return p, key


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
    G[edge[0]].append((edge[1], edge[2]))

p, key = djkistra(G, 0)

for i in range(0, len(p)):
    if p[i] is not None or i == 0:
        print(str(i)+ "|" + str(key[i]) + "|"+construir_camino(p, i, 0))