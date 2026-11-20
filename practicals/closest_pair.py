import math

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force(points):
    best = float("inf")
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            best = min(best, distance(points[i], points[j]))
    return best

def closest_pair(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)

    mid = n // 2
    left_x = px[:mid]
    right_x = px[mid:]
    mid_x = px[mid][0]
    left_set = set(left_x)
    left_y = [p for p in py if p in left_set]
    right_y = [p for p in py if p not in left_set]

    d = min(closest_pair(left_x, left_y), closest_pair(right_x, right_y))
    strip = [p for p in py if abs(p[0] - mid_x) < d]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            d = min(d, distance(strip[i], strip[j]))
    return d

points = [tuple(map(float, input("Enter x and y coordinates: ").split())) for _ in range(int(input("Number of points: ")))]
if len(points) < 2:
    print("At least two points are required.")
else:
    print("Closest pair distance:", closest_pair(sorted(points), sorted(points, key=lambda p: p[1])))
