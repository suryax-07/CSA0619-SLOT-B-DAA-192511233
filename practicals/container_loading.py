def container_loading(weights, capacity):
    selected = []
    total = 0
    for index, weight in sorted(enumerate(weights), key=lambda item: item[1]):
        if total + weight <= capacity:
            selected.append(index + 1)
            total += weight
    return selected, total

weights = list(map(int, input("Enter container weights: ").split()))
capacity = int(input("Enter ship capacity: "))
selected, total = container_loading(weights, capacity)
print("Selected container numbers:", selected)
print("Total loaded weight:", total)
