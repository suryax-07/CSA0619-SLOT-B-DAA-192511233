
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 +
                     (p1[1] - p2[1])**2)

def closest_pair(points):
    n = len(points)

    if n <= 3:
        minimum = float('inf')
        pair = None

        for i in range(n):
            for j in range(i + 1, n):
                d = distance(points[i], points[j])
                if d < minimum:
                    minimum = d
                    pair = (points[i], points[j])

        return minimum, pair

    mid = n // 2
    left = points[:mid]
    right = points[mid:]

    d1, pair1 = closest_pair(left)
    d2, pair2 = closest_pair(right)

    if d1 < d2:
        minimum, pair = d1, pair1
    else:
        minimum, pair = d2, pair2

    mid_x = points[mid][0]
    strip = [p for p in points
             if abs(p[0] - mid_x) < minimum]

    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= minimum:
                break

            d = distance(strip[i], strip[j])

            if d < minimum:
                minimum = d
                pair = (strip[i], strip[j])

    return minimum, pair


n = int(input("Enter number of points: "))

points = []

for i in range(n):
    x, y = map(int, input("Enter x and y: ").split())
    points.append((x, y))

points.sort()

d, pair = closest_pair(points)

print("Closest Pair:", pair)
print("Minimum Distance:", round(d, 2))
