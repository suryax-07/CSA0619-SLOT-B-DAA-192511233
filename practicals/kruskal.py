def kruskal(vertices, edges):
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
    for u, v, w in sorted(edges, key=lambda edge: edge[2]):
        if union(u, v):
            mst.append((u, v, w))
    return mst, sum(edge[2] for edge in mst)

v = int(input("Number of vertices: "))
e = int(input("Number of edges: "))
edges = []
print("Enter edges as: source destination weight (vertices start at 0)")
for _ in range(e):
    edges.append(tuple(map(int, input().split())))
mst, total = kruskal(v, edges)
print("MST edges:", mst)
print("Total weight:", total)
