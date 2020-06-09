#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    for row in range(n):
        triangle += [[1 for col in range(row + 1)]]

    for row in range(n):
        for c in range(row):
            triangle[row][c + 1] = sum(triangle[row - 1][c:c + 2])
    return triangle


triangle = pascal_triangle(7)
for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))