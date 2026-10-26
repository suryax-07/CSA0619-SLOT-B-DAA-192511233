def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    p1 = karatsuba(a, c)
    p2 = karatsuba(b, d)
    p3 = karatsuba(a + b, c + d)

    return p1 * (10 ** (2 * m)) + (p3 - p1 - p2) * (10 ** m) + p2

x = 1234
y = 5678

print("Product:", karatsuba(x, y))
