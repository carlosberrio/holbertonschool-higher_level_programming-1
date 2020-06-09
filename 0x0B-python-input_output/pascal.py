n = 5
def pascal_triangle(n):
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows

triangle = pascal_triangle(n)
for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))