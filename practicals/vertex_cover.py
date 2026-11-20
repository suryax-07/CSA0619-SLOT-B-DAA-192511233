def greedy_vertex_cover(vertices, edges):
    remaining = set(tuple(edge) for edge in edges)
    cover = set()
    while remaining:
        degree = {}
        for u, v in remaining:
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1
        chosen = max(degree, key=degree.get)
        cover.add(chosen)
        remaining = {(u, v) for u, v in remaining if u != chosen and v != chosen}
    return cover

v = int(input("Number of vertices: "))
e = int(input("Number of edges: "))
edges = []
print("Enter each edge as two vertex numbers:")
for _ in range(e):
    edges.append(tuple(input().split()))
print("Approximate vertex cover:", greedy_vertex_cover(range(v), edges))
