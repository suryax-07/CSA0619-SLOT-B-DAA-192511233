def tsp(graph, start=0):
    n = len(graph)
    dp = {(1 << start, start): (0, [start])}

    for mask in range(1 << n):
        for last in range(n):
            state = (mask, last)
            if state not in dp:
                continue
            cost, path = dp[state]
            for nxt in range(n):
                if not mask & (1 << nxt) and graph[last][nxt] != float("inf"):
                    new_mask = mask | (1 << nxt)
                    new_cost = cost + graph[last][nxt]
                    key = (new_mask, nxt)
                    if key not in dp or new_cost < dp[key][0]:
                        dp[key] = (new_cost, path + [nxt])

    full = (1 << n) - 1
    choices = [(dp[(full, last)][0] + graph[last][start], dp[(full, last)][1] + [start])
               for last in range(n) if (full, last) in dp and graph[last][start] != float("inf")]
    return min(choices) if choices else (None, [])

n = int(input("Number of cities: "))
print("Enter adjacency matrix (use 999999 for no direct route):")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append([float("inf") if x == 999999 else x for x in row])
cost, path = tsp(graph)
print("Minimum tour cost:", cost)
print("Tour:", path)
