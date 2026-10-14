def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    left = [x for x in a[1:] if x <= pivot]
    right = [x for x in a[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


a = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", quick_sort(a))