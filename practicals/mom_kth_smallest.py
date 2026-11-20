def select_kth(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the number of elements")
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]
    pivot = select_kth(medians, (len(medians) + 1) // 2)

    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]

    if k <= len(low):
        return select_kth(low, k)
    if k <= len(low) + len(equal):
        return pivot
    return select_kth(high, k - len(low) - len(equal))

values = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))
print("Kth smallest element:", select_kth(values, k))
