def subset_sum_mitm(values, target):
    n = len(values)
    mid = n // 2
    left = values[:mid]
    right = values[mid:]

    left_sums = {}
    for mask in range(1 << len(left)):
        total = sum(left[i] for i in range(len(left)) if mask & (1 << i))
        left_sums.setdefault(total, mask)

    for mask in range(1 << len(right)):
        total = sum(right[i] for i in range(len(right)) if mask & (1 << i))
        needed = target - total
        if needed in left_sums:
            left_mask = left_sums[needed]
            result = [left[i] for i in range(len(left)) if left_mask & (1 << i)]
            result += [right[i] for i in range(len(right)) if mask & (1 << i)]
            return result
    return None

values = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))
answer = subset_sum_mitm(values, target)
print("Subset found:", answer if answer is not None else "No subset exists")
