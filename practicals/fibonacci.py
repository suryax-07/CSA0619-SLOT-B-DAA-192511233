def fibonacci(n):
    if n < 0:
        raise ValueError("Enter a non-negative number")
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Number of terms: "))
print("Fibonacci series:", *fibonacci(n))
