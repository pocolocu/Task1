def generate_pascals_triangle(n: int) -> list[list[int]]:
    triangle = [[1] * (i + 1) for i in range(n)]
    
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    return triangle

n = 5
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(row)
