def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda item: item[1] / item[0], reverse=True)
    total = 0
    for weight, value in items:
        if capacity == 0:
            break
        take = min(weight, capacity)
        total += take * value / weight
        capacity -= take
    return total

weights = list(map(float, input("Enter weights: ").split()))
values = list(map(float, input("Enter values: ").split()))
capacity = float(input("Enter capacity: "))
print("Maximum value:", fractional_knapsack(weights, values, capacity))
