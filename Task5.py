def area_triangle(a, b, c):
    a = float(input(1))
    b = float(input(2))
    c = float(input(3))

    s = float((a + b + c) / 2)

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print (area_triangle(1, 2, 3))
