import heapq

def prim(graph, start=0):
    n = len(graph)
    visited = [False] * n
    heap = [(0, start, -1)]
    mst = []
    total = 0
    while heap and len(mst) < n - 1:
        weight, u, parent = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, weight))
            total += weight
        for v, w in enumerate(graph[u]):
            if not visited[v] and w >= 0 and w != float("inf"):
                heapq.heappush(heap, (w, v, u))
    return mst, total

n = int(input("Number of vertices: "))
print("Enter adjacency matrix (use -1 for no edge):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append([float("inf") if x == -1 else x for x in row])
edges, total = prim(graph)
print("MST edges:", edges)
print("Total weight:", total)
