def greedy_set_cover(universe, subsets):
    uncovered = set(universe)
    chosen = []
    while uncovered:
        best = max(subsets, key=lambda subset: len(uncovered & subset), default=set())
        gain = uncovered & best
        if not gain:
            return None
        chosen.append(best)
        uncovered -= gain
    return chosen

universe = set(input("Enter universe elements separated by spaces: ").split())
count = int(input("Number of subsets: "))
subsets = []
for i in range(count):
    subsets.append(set(input("Enter subset " + str(i + 1) + ": ").split()))
answer = greedy_set_cover(universe, subsets)
print("Selected subsets:", answer if answer is not None else "No cover exists")
