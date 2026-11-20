def graph_coloring(graph, colors):
    n = len(graph)
    result = [-1] * n

    def safe(vertex, color):
        return all(not graph[vertex][other] or result[other] != color for other in range(n))

    def assign(vertex):
        if vertex == n:
            return True
        for color in range(colors):
            if safe(vertex, color):
                result[vertex] = color
                if assign(vertex + 1):
                    return True
                result[vertex] = -1
        return False

    return result if assign(0) else None

n = int(input("Number of vertices: "))
print("Enter adjacency matrix (0 or 1):")
graph = [list(map(int, input().split())) for _ in range(n)]
m = int(input("Number of colors: "))
answer = graph_coloring(graph, m)
print("Color assignment (0-based):", answer if answer else "No valid coloring")
