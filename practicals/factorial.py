def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))
