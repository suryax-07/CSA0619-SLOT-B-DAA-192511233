def bellman_ford(vertices, edges, source):
    distance = [float("inf")] * vertices
    distance[source] = 0

    for _ in range(vertices - 1):
        changed = False
        for u, v, weight in edges:
            if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                changed = True
        if not changed:
            break

    for u, v, weight in edges:
        if distance[u] != float("inf") and distance[u] + weight < distance[v]:
            return None
    return distance

v = int(input("Number of vertices: "))
e = int(input("Number of edges: "))
edges = []
print("Enter each edge as: source destination weight (vertices start at 0)")
for _ in range(e):
    edges.append(tuple(map(int, input().split())))
source = int(input("Source vertex: "))
result = bellman_ford(v, edges, source)
if result is None:
    print("Negative weight cycle detected.")
else:
    print("Shortest distances:", result)
