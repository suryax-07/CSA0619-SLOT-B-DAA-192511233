def hamiltonian_cycle(graph):
    n = len(graph)
    path = [0]

    def search():
        if len(path) == n:
            return graph[path[-1]][path[0]] == 1
        for vertex in range(1, n):
            if vertex not in path and graph[path[-1]][vertex] == 1:
                path.append(vertex)
                if search():
                    return True
                path.pop()
        return False

    if search():
        return path + [path[0]]
    return None

n = int(input("Number of vertices: "))
print("Enter adjacency matrix (0 or 1):")
graph = [list(map(int, input().split())) for _ in range(n)]
answer = hamiltonian_cycle(graph)
print("Hamiltonian cycle:", answer if answer else "No cycle exists")
