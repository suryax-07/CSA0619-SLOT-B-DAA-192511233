def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]
    prefix = [0]
    for f in freq:
        prefix.append(prefix[-1] + f)

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = prefix[j + 1] - prefix[i]
            best = float("inf")
            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0
                if left + right + total < best:
                    best = left + right + total
                    root[i][j] = r
            cost[i][j] = best
    return cost[0][n - 1] if n else 0, root

keys = input("Enter sorted keys: ").split()
freq = list(map(int, input("Enter search frequencies: ").split()))
if len(keys) != len(freq):
    print("Number of keys and frequencies must match.")
else:
    cost, roots = optimal_bst(keys, freq)
    print("Minimum search cost:", cost)
    if keys:
        print("Root key:", keys[roots[0][len(keys) - 1]])
