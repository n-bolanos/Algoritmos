import heapq

def prim(G, r):
    peso_total = 0
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
        peso_total += peso

        for v, weight in G[u]:
            if not encontrado[v] and weight < key[v]:
                p[v] = u
                key[v] = weight
                heapq.heappush(Q, (key[v], v))
                
    
    return peso_total, p, key


config = [int(i) for i in input().split()]
G = [[] for _ in range(config[0])]

for _ in range(config[1]):
    edge = [int(i) for i in input().split()]
    G[edge[0]].append((edge[1], edge[2]))
    G[edge[1]].append((edge[0], edge[2]))

peso, p, key = prim(G, 0)
print(peso)
for nodo in p.keys():
    if nodo == 0:
        continue
    print(f'({p[nodo]},{nodo}) {key[nodo]}')
