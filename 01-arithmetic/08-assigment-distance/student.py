def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

point1 = (1, 2)
point2 = (4, 6)

dist = distance(point1[0], point1[1], point2[0], point2[1])
print(f"The distance between the points is: {dist}")