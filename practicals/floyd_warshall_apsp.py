def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n = int(input("Number of vertices: "))
print("Enter adjacency matrix (use 999999 where no edge exists):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append([float("inf") if x == 999999 else x for x in row])
result = floyd_warshall(graph)
print("All-pairs shortest distance matrix:")
for row in result:
    print(["INF" if x == float("inf") else x for x in row])
