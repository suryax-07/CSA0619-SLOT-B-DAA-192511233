def first_fit_decreasing(items, capacity):
    bins = []
    for item in sorted(items, reverse=True):
        placed = False
        for index in range(len(bins)):
            if bins[index] + item <= capacity:
                bins[index] += item
                placed = True
                break
        if not placed:
            bins.append(item)
    return bins

items = list(map(int, input("Enter item sizes: ").split()))
capacity = int(input("Enter bin capacity: "))
if any(item > capacity or item <= 0 for item in items):
    print("Each item must be positive and no larger than bin capacity.")
else:
    bins = first_fit_decreasing(items, capacity)
    print("Bins used:", len(bins))
    print("Bin loads:", bins)
