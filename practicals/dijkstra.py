import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float("inf")] * n
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        current, u = heapq.heappop(pq)
        if current != dist[u]:
            continue
        for v, weight in enumerate(graph[u]):
            if weight >= 0 and weight != float("inf"):
                new_dist = current + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    return dist

n = int(input("Number of vertices: "))
print("Enter adjacency matrix (use -1 for no edge):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append([float("inf") if x == -1 else x for x in row])
source = int(input("Source vertex (0-based): "))
print("Shortest distances:", dijkstra(graph, source))
