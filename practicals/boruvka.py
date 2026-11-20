def boruvka(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    mst = []
    components = vertices
    while components > 1:
        cheapest = [None] * vertices
        for edge in edges:
            u, v, w = edge
            a, b = find(u), find(v)
            if a != b:
                if cheapest[a] is None or w < cheapest[a][2]:
                    cheapest[a] = edge
                if cheapest[b] is None or w < cheapest[b][2]:
                    cheapest[b] = edge
        added = False
        for edge in cheapest:
            if edge is not None and union(edge[0], edge[1]):
                mst.append(edge)
                components -= 1
                added = True
        if not added:
            break
    return mst, sum(edge[2] for edge in mst)

v = int(input("Number of vertices: "))
e = int(input("Number of edges: "))
edges = []
print("Enter edges as: source destination weight (vertices start at 0)")
for _ in range(e):
    edges.append(tuple(map(int, input().split())))
mst, total = boruvka(v, edges)
print("MST edges:", mst)
print("Total weight:", total)
